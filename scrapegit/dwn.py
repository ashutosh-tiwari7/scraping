from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
options = Options()
dr = webdriver.Chrome(options=options)
y = '''
https://www.instagram.com/reel/DJ-us_zSvfc/?igsh=MXdzenh0Z2p3azN0eA==
https://www.instagram.com/reel/DJ7VMSQzHbv/?igsh=MXd2OTNqYzgwb3FnNw==
https://www.instagram.com/reel/DDiW4i2S-V2/?igsh=MWlubnVqODQ4eG45Mw==
https://www.instagram.com/reel/DEh01GfvDjj/?igsh=M215eHFhdGJmNjV3
https://www.instagram.com/reel/DJVdTuZiBio/?igsh=MWlpMDdtdnpua3d0YQ==
https://www.instagram.com/reel/DJLMnaSqmRs/?igsh=ZnM5ajIzaHR5eHNm
https://www.instagram.com/reel/DJRW1gCR54N/?igsh=MW5nc2d2NnVvaHJteg==
https://www.instagram.com/reel/DGBEqORy0in/?igsh=MXZvNDdsYnZiNmZiZw==
https://www.instagram.com/reel/DEckMC1BSli/?igsh=NHowdTNvbThzMzRs
https://www.instagram.com/reel/DF-C-FLTIrg/?igsh=enplcHFyeW15eDgx
https://www.instagram.com/reel/DH0m-x1vLF_/?igsh=YXhsaGE4NnF4dDN2
https://www.instagram.com/reel/DHLzh-Bzdvf/?igsh=MXZiNGlpYWEwNnpiNA==
https://www.instagram.com/reel/DFX7AHwoBc_/?igsh=cXgycnFidnc0ZjB5
https://www.instagram.com/reel/DIga7tJSAgR/?igsh=a3FyajQwZ3kybGx1
https://www.instagram.com/reel/DDUVfF8vCVC/?igsh=MWtuazU2bXN2NmhtYg==
https://www.instagram.com/reel/DIBcM6XsuOn/?igsh=MWhxMG4wY2swZXN0cw==
https://www.instagram.com/reel/DDznjG7Pays/?igsh=MXFwMmRkM2g4aW44Yw==
https://www.instagram.com/reel/DH1Hl8XObJz/?igsh=MWNnd3RxZWJvcm5kbg==
https://www.instagram.com/reel/DIt1_zBy8xu/?igsh=MXZ2bGxna2FiaGowYw==
https://www.instagram.com/reel/DG48mervcF6/?igsh=MWdjd3FpbzU4b2ltMw==
https://www.instagram.com/reel/DHIxNW4yBqg/?igsh=bDA5YXl0M3ZsMGI4
https://www.instagram.com/reel/DHvh9Xyus1A/?igsh=NDh3NmhhYnduamZ0
https://www.instagram.com/reel/DIgg_ZOyfuL/?igsh=MWdwejhiNjl0b3V1Yw==
https://www.instagram.com/reel/DIYS91oIe5u/?igsh=aHFuOHV6cDRsYXA1
https://www.instagram.com/reel/DIPN9Evq4rd/?igsh=dDhvNDI1eXhodTQ2
https://www.instagram.com/reel/DEOvAW2IsFY/?igsh=dTBnMW1meGtpdnFi
https://www.instagram.com/reel/DIUQECWNh2N/?igsh=MWY5NWZiM3pnaWpqMA==
https://www.instagram.com/reel/DEUcckdyDtt/?igsh=MWk0NWZpdXUzOHV3bA==
https://www.instagram.com/reel/DHli7S-yvIK/?igsh=MWN0OGM2bHFvNHdvdA==
https://www.instagram.com/reel/DGDeaXPpqNl/?igsh=NDc0MHJ5bHpjcHcy
https://www.instagram.com/reel/DHtgNoSMRqG/?igsh=MTRhMzJ6ODJ5eWpmaA==
https://www.instagram.com/reel/DE-nHYEOB7R/?igsh=OG1zb3I5aDZ0NWZi
https://www.instagram.com/reel/DIQDNPqhkYc/?igsh=MW1kNXVubGV3a3k0Ng==
https://www.instagram.com/reel/DCFd4G1xIOW/?igsh=N25hZmljcGFjZm05
https://www.instagram.com/reel/DBzAozmxRNR/?igsh=MWU5azBneTNvYTJrYQ==
https://www.instagram.com/reel/DFNsRI_yKBX/?igsh=dDh4YWNuYmc4NTVm
https://www.instagram.com/reel/DGlsowFS42m/?igsh=cjV0em1ja2xyOG1n
https://www.instagram.com/reel/DFobY0zR8mS/?igsh=b2s2dDY1MnNqODcx
https://www.instagram.com/reel/DDKr-5oS1Mx/?igsh=MTlpa3hteDJwbjhxYQ==
https://www.instagram.com/reel/DCZbP6pSnzn/?igsh=dHhvdTZwNWVtanM5
https://www.instagram.com/reel/DDx-4qTKC-p/?igsh=MWZxbDYweXd4Ynh0Nw==
https://www.instagram.com/reel/DDo55GZhttT/?igsh=dG0ydmU0ZnBnNndp
https://www.instagram.com/reel/DBZwn3TiQV-/?igsh=MTF3MmRwN283MTFncw==
https://www.instagram.com/reel/DE5ejasi84K/?igsh=Z21zeGJncnNqMXox
https://www.instagram.com/reel/DGqB3kYNOox/?igsh=MXZ4cHVhdHp6ZHAyYw==
https://www.instagram.com/reel/DHG6QTWoEuj/?igsh=MXFramttOHRhZm9ucg==
https://www.instagram.com/reel/DHXeHZXo9vp/?igsh=Z3NvbWM2bzVweDg=
https://www.instagram.com/reel/DG91gzXIiop/?igsh=cjJ5N3J5YnU4dDZ6
https://www.instagram.com/reel/DKSS91ICZ2B/?igsh=MWt3MzYwbXE3b3Nyaw==
https://www.instagram.com/reel/DKQCBPSu3Ew/?igsh=cGExcHk0dXNkam4=
https://www.instagram.com/reel/DFhh-BtxwpX/?igsh=MTcwczFneGNrcmh2dw==
https://www.instagram.com/reel/DKHn8jzPC9l/?igsh=OGJ0YjljNWw0ang4
https://www.instagram.com/reel/DKFRqsuIten/?igsh=ODNuYTlzbGR6bTBp
https://www.instagram.com/reel/DKL3-RHMlnQ/?igsh=Y2xwYzVnb2M4czB4
https://www.instagram.com/reel/DKKHazuic8n/?igsh=MWJ3eDRiNXZxaThhOA==
https://www.instagram.com/reel/DESa86nCah1/?igsh=MXRheHUxZnRyNmt3dA==
https://www.instagram.com/reel/DFhL7X1ouaG/?igsh=ZHk2eTRsbjF2eHlq
https://www.instagram.com/reel/DKSB5b6IMZN/?igsh=MXdqa2diaHd0cG9heA==
https://www.instagram.com/reel/DKOKNp1TRhD/?igsh=MTNod20ycmVydGw5bw==
https://www.instagram.com/reel/DKQfYjGSbqE/?igsh=MWs0cXhiZXhsdnUyMw==
https://www.instagram.com/reel/DKQrqVVh1Gs/?igsh=ZnlibGtxdzBvOTQ1
https://www.instagram.com/reel/DKRYfScpzqx/?igsh=bzZpZWZ6MmsydTN4
https://www.instagram.com/reel/DKF0StBIlfL/?igsh=MWdyaTJhMHpnNmNmNQ==
https://www.instagram.com/reel/DDcanRrzxpq/?igsh=d2g1d240enNlNGJr
https://www.instagram.com/reel/DEfsFShO7J6/?igsh=MTViM2I5bmQ3N2Yzeg==
https://www.instagram.com/reel/DFx2a-7uw0M/?igsh=MXZtcGY1bWo5OXNqZw==
https://www.instagram.com/reel/DJo_StCCAsw/?igsh=MWd1ZW00bHc5djl0MQ==
https://www.instagram.com/reel/DDsk4q_v4lP/?igsh=MWRrZXJ2ZHY4NGJ5aA==
https://www.instagram.com/reel/DKSPI7-C5wM/?igsh=MWd0ZW82eWE3Nm5zcg==
https://www.instagram.com/reel/DDuXHCQyfgB/?igsh=MXZ3bXM4cGg5dHY1OA==
https://www.instagram.com/reel/DGa_UZ6ALJa/?igsh=dHlhcDd4aWMzMmxk
https://www.instagram.com/reel/DKPbAUzSZlP/?igsh=MWFzemloOTMyY2czcA==
https://www.instagram.com/reel/DJiL8ixPbJk/?igsh=dzQzYW94NmFlMDBt
https://www.instagram.com/reel/DKUdRtSsNM1/?igsh=NjZoZjFoeHgzZWg4
https://www.instagram.com/reel/DDLW41kiFGa/?igsh=MzN5dnEzeXUzcDZn
https://www.instagram.com/reel/DFrFp48g1la/?igsh=MXE1b2hta2U4bnEwbA==
https://www.instagram.com/reel/DKUggrCoBxm/?igsh=MWxhcHY5YzltZXlyMA==
https://www.instagram.com/reel/DIHg9SuhSz3/?igsh=cHRta3F5ZWV6aDI5
https://www.instagram.com/reel/DKSMr1HJsCx/?igsh=MTAybGlvdWw3M2lvYw==
https://www.instagram.com/reel/DKNhm8-zX8k/?igsh=cTF4aWdhcTV0a3Z6
https://www.instagram.com/reel/DKKdHTZgmqN/?igsh=MzVvand6OXh6MjRp
https://www.instagram.com/reel/DKAP3TfPsOs/?igsh=ODJycHF2OWVxMHdz
https://www.instagram.com/reel/DJ7KAx-Poic/?igsh=amR0Ym9hZjFudnY4
https://www.instagram.com/reel/DIgfSpzgJ-V/?igsh=ZnlxcThwcTNyd3lo
https://www.instagram.com/reel/DFqMtpDNYP0/?igsh=dnFka202b3E5OTg5
https://www.instagram.com/reel/DKPkSFqBy5N/?igsh=MTVwbzh4dXcyb3c1ZQ==
https://www.instagram.com/reel/DEimf89iCY4/?igsh=dzNxN3hjYTBoZ2ox
https://www.instagram.com/reel/DF74PzDiVpW/?igsh=MTh2MWNrb2tjb2pkMg==
https://www.instagram.com/reel/DHbU2Vfza-F/?igsh=MThhNnJmcHkxN2F1OA==
https://www.instagram.com/reel/DHgcI3WiLPB/?igsh=YTVvMTM4cWFjamR1
https://www.instagram.com/reel/DGY8Y9LC35g/?igsh=MW16bmdjaDkyN21qcw==
https://www.instagram.com/reel/DE2UwRNxdlt/?igsh=czNta2Q5cGtqZWw1
https://www.instagram.com/reel/DKQNNJpiu5S/?igsh=MXZ6cWNodGFzM3J2aw==
https://www.instagram.com/reel/DKHnhrxIOT8/?igsh=MXVud3NuY2c1aDYwdA==
https://www.instagram.com/reel/DKM_CKfxdUb/?igsh=MWQ3eXl5dWtkZnVnNg==
https://www.instagram.com/reel/DKUbuw6Ju66/?igsh=MW50YTh2ZXUzd3B5Zw==
https://www.instagram.com/reel/DF5yMLxJaxv/?igsh=dHJnbWF5Zm5pNDM0
https://www.instagram.com/reel/DKJaMJQzUz3/?igsh=MWIwbWdsNml1czRtdA==
https://www.instagram.com/reel/DJhHP-GI5Q1/?igsh=bW84YTgybngxZ2ls
https://www.instagram.com/reel/DG0pChCovMp/?igsh=OGRsOThmczU0cWph
https://www.instagram.com/reel/DDuHCEDA1Ml/?igsh=MTlwdmk0eDBoYWI5cQ==
https://www.instagram.com/reel/DE4Mf9gxD4k/?igsh=ZG11Z3UxbGxkZWlp
https://www.instagram.com/reel/DKOpV6Lslyj/?igsh=bWtiM3Ywa29sdXZ4
https://www.instagram.com/reel/DKRUVu8PMSn/?igsh=Z2RucDZ2d2tzMmpu
https://www.instagram.com/reel/DE2ghAbCzVy/?igsh=MTd0Y3JzenczdnE4aw==
https://www.instagram.com/reel/DDxOtRiik6H/?igsh=MXVvNWowMTR4M3UzNA==
https://www.instagram.com/reel/DHE55lBI_Ng/?igsh=MWZ4OGdiNXNrZmcxNQ==
https://www.instagram.com/reel/DDx1dUzgWR3/?igsh=MXZxMXlxY2oxeXYzYg==
https://www.instagram.com/reel/DKUgb3TvK3F/?igsh=MTEza3ZtYTNuZmFqYQ==
https://www.instagram.com/reel/DFQM1-MSQMh/?igsh=bDVtOHdvNWphaHln
https://www.instagram.com/reel/DJ82MbSTkgN/?igsh=dWFpZDNpMzEwZHls
https://www.instagram.com/reel/DJ9jSKzoLBv/?igsh=MWY1czExYzY0ZDQ0eg==
https://www.instagram.com/reel/DJIXB3rM-E_/?igsh=eXJzdDNqeWFwb3I4
https://www.instagram.com/reel/DKGFtUhTLKF/?igsh=aDdyYWZnMzQzcGRh
https://www.instagram.com/reel/DKUj6lQoH6m/?igsh=MnFqbDdrZzU1Nmlx
https://www.instagram.com/reel/DHCuCQWSqMT/?igsh=OXMxeWUyMnR3aXI4
https://www.instagram.com/reel/DEiVVcEtbmX/?igsh=djE1M2wzOXl5Zndw
https://www.instagram.com/reel/DHOnG2OCc6P/?igsh=eG1yajA3bnh0Nzhs
https://www.instagram.com/reel/DE47uPltB0w/?igsh=MWs5a2I0aG9leDFiYQ==
https://www.instagram.com/reel/DFlAr-dsktz/?igsh=MTVzdHAyMm5oZ2k1ZQ==
https://www.instagram.com/reel/DDjcN1aMAPC/?igsh=MWc5aTBlZTRsZHEwaA==
https://www.instagram.com/reel/DKNCfT_Nn6m/?igsh=cmZoM3drYnA4YXJn
https://www.instagram.com/reel/DKE8vPmSv2V/?igsh=N3ZndzNuMjBrcWl0
https://www.instagram.com/reel/DKIGIxhImm7/?igsh=MjFlYjF5d3dlb2t2
https://www.instagram.com/reel/DJyJkUKv1LW/?igsh=dWk0enBoZGQwdTkx
'''.split('\n')
i = 1
for xx in y:
    if xx != '':
        if i > 15 :
            print(i)
            i+=1
            dr.get('https://indown.io/')
            dr.maximize_window()
            inp = dr.find_element(By.ID, "link")
            inp.send_keys(xx)
            inp2 = dr.find_element(By.ID, "get")
            inp2.click()
            time.sleep(10)
            try :
                inpx = dr.find_elements(By.CLASS_NAME, "btn-group-vertical")
                inp3 = inpx[0].find_elements(By.TAG_NAME, "a")
                inp3[0].click()
            except :
                time.sleep(10)
                inpx = dr.find_elements(By.CLASS_NAME, "btn-group-vertical")
                inp3 = inpx[0].find_elements(By.TAG_NAME, "a")
                inp3[0].click()
            time.sleep(10)
        else :
            i+= 1
