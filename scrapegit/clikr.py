from selenium import webdriver

#start PhantomJS
service_args = [ '--proxy=101.109.143.71:36127', '--proxy-type=https', ]
driver = webdriver.PhantomJS(service_args=service_args, executable_path='/home/diablo/Downloads/phantomjs-2.1.1-linux-x86_64(1)/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')

driver.get('http://icanhazip.com')

driver.save_screenshot("screenshot1.png")

service_args = [ '--proxy=100.39.36.100:35531', '--proxy-type=https', ]
driver = webdriver.PhantomJS(service_args=service_args, executable_path='/home/diablo/Downloads/phantomjs-2.1.1-linux-x86_64(1)/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')

driver.get('http://icanhazip.com')

driver.save_screenshot("screenshot2.png")

