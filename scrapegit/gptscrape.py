# This project is for education purpose only

import asyncio
import json
import os
import random
import string
import time
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from playwright.sync_api import Playwright, sync_playwright, TimeoutError as PWTimeout
from threading import Lock


CHAT_URL = "https://chat.openai.com/chat" 
DATA_DIR = Path("sessions")
DATA_DIR.mkdir(exist_ok=True)
MAX_RETRIES = 3
DELAY_RANGE = (1.0, 2.5) 
NAV_TIMEOUT = 30000  
REPLY_TIMEOUT = 60 
CONCURRENT_SESSIONS = 3

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
    " Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0) AppleWebKit/605.1.15 (KHTML, like Gecko)"
    " Version/16.0 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)"
    " Chrome/120.0.0.0 Safari/537.36",
]

browser_lock = Lock() 
session_locks = {} 
global_semaphore = asyncio.Semaphore(CONCURRENT_SESSIONS)

app = FastAPI(title="Chat Scraper API (Playwright)", version="0.1")


class ChatRequest(BaseModel):
    prompt: str
    session_id: Optional[str] = None
    max_wait: Optional[int] = REPLY_TIMEOUT  # seconds to wait for reply


def random_delay():
    time.sleep(random.uniform(*DELAY_RANGE))


def random_user_agent():
    return random.choice(USER_AGENTS)


def _random_session_id(length=12):
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=length))


class BrowserManager:

    def __init__(self):
        self.playwright: Optional[Playwright] = None
        self.browser = None

    def start(self):
        if self.playwright is None:
            self.playwright = sync_playwright().start()
            self.browser = self.playwright.chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled"])
        return self.browser

    def stop(self):
        if self.browser:
            self.browser.close()
            self.browser = None
        if self.playwright:
            self.playwright.stop()
            self.playwright = None

    def get_or_create_context(self, session_id: str, user_agent: str):
        DATA_DIR.mkdir(exist_ok=True)
        storage_path = DATA_DIR / f"{session_id}.json"
        options = {
            "user_agent": user_agent,
            "viewport": {"width": 1200, "height": 800},
            "java_script_enabled": True,
        }

        if storage_path.exists():
            context = self.browser.new_context(storage_state=str(storage_path), **options)
        else:
            context = self.browser.new_context(**options)

        return context, storage_path

    def save_storage(self, context, storage_path: Path):
        try:
            context.storage_state(path=str(storage_path))
        except Exception as e:
            print(f"Warning: failed to save storage for {storage_path}: {e}")

manager = BrowserManager()

def ensure_session_lock(session_id: str):
    if session_id not in session_locks:
        session_locks[session_id] = Lock()
    return session_locks[session_id]


def send_prompt_and_scrape(context, target_url: str, prompt: str, max_wait: int = REPLY_TIMEOUT):
    page = context.new_page()
    try:
        page.set_default_navigation_timeout(NAV_TIMEOUT)
        page.set_default_timeout(NAV_TIMEOUT)

        random_delay()

        page.goto(target_url, wait_until="domcontentloaded")
        random_delay()

        possible_textarea_selectors = [
            'textarea[name="prompt-textarea"]',
            'textarea[placeholder*="Ask Anything"]',
            'div[role="textbox"]',
            'div[id="prompt-textarea"]',
        ]

        textarea = None
        for sel in possible_textarea_selectors:
            try:
                el = page.query_selector(sel)
                if el:
                    textarea = el
                    break
            except PWTimeout:
                continue

        if textarea is None:
            page.wait_for_timeout(2000)
            textarea = page.query_selector("textarea")

        if textarea is None:
            raise RuntimeError("Input textarea/box not found on page.")

        textarea.click()
        for ch in prompt:
            textarea.type(ch)
            time.sleep(random.uniform(0.01, 0.06))

        random_delay()

        try:
            textarea.press("Enter")
        except Exception:
            send_button_selectors = [
                Send prompt
                'button[id="composer-submit-button"]',
                'button[aria-label="Send prompt"]',
            ]
            clicked = False
            for s in send_button_selectors:
                btn = page.query_selector(s)
                if btn:
                    btn.click()
                    clicked = True
                    break
            if not clicked:
                textarea.press("Control+Enter")

        start_time = time.time()
        reply_text = None

        reply_selectors = [
            'div[data-testid="assistant-response"]',
            'div[data-message-model-slug="gpt-4o"]',
        ]

        while time.time() - start_time < max_wait:
            page.wait_for_timeout(5000)
            random_delay()

            for sel in reply_selectors:
                elems = page.query_selector_all(sel)
                if elems:
                    last = elems[-1]
                    text = last.inner_text().strip()
                    if text:
                        reply_text = text
                        break
            if reply_text:
                break

            all_divs = page.query_selector_all("div")
            
            for d in reversed(all_divs):
                try:
                    txt = d.inner_text().strip()
                    if len(txt) > 20: 
                        reply_text = txt
                        break
                except Exception:
                    continue
            if reply_text:
                break

        if reply_text is None:
            raise RuntimeError("Timed out waiting for assistant reply")

        metadata = {
            "scrape_time": time.time(),
            "extracted_selector_guess": sel if 'sel' in locals() else None,
        }
        return reply_text, metadata
    finally:
        try:
            page.close()
        except Exception:
            pass


@app.post("/chat")
async def chat_endpoint(req: ChatRequest, request: Request):
    """
    Example POST payload:
    {
        "prompt": "What is python",
    }
    Response:
    {
      "session_id",
      "prompt",
      "response",
      "metadata"
    }
    """
    if not req.prompt or not req.prompt.strip():
        raise HTTPException(status_code=400, detail="prompt must be provided")

    session_id = req.session_id or _random_session_id()
    session_lock = ensure_session_lock(session_id)

    await global_semaphore.acquire()
    try:
        session_lock.acquire()
        try:
            with browser_lock:
                manager.start()

            ua = random_user_agent()
            context, storage_path = manager.get_or_create_context(session_id, ua)

            last_exc = None
            for attempt in range(1, MAX_RETRIES + 1):
                try:
                    random_delay()

                    reply_text, metadata = send_prompt_and_scrape(context, CHAT_URL, req.prompt, req.max_wait)

                    manager.save_storage(context, storage_path)

                    try:
                        context.close()
                    except Exception:
                        pass

                    return {
                        "session_id": session_id,
                        "prompt": req.prompt,
                        "response": reply_text,
                        "metadata": {
                            "attempts": attempt,
                            "storage_path": str(storage_path),
                            **metadata,
                        },
                    }

                except (PWTimeout, RuntimeError) as e:
                    last_exc = e
                    backoff = 1.5 * attempt
                    time.sleep(backoff + random.uniform(0.2, 0.7))
                    try:
                        context.close()
                    except Exception:
                        pass
                    context, storage_path = manager.get_or_create_context(session_id, ua)
                    continue
                except Exception as e:
                    # fatal error
                    last_exc = e
                    try:
                        context.close()
                    except Exception:
                        pass
                    raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")

            raise HTTPException(status_code=500, detail=f"Failed after {MAX_RETRIES} attempts: {last_exc}")
        finally:
            session_lock.release()
    finally:
        global_semaphore.release()


@app.on_event("shutdown")
def shutdown_event():
    try:
        manager.stop()
    except Exception:
        pass
