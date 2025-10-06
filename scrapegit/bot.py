import selenium
from selenium import webdriver

pth = r'/home/diablo/chromedriver'
dri = webdriver.Chrome(pth)

dri.get('https://free-proxy-list.net/')
prox = []
proxt = dri.find_elements_by_xpath('//*[@id="proxylisttable"]/tbody/tr')
for x in proxt:
	row_data = x.find_elements_by_tag_name('td')
	proxy = row_data[0].text+":"+row_data[1].text
	prox.append(proxy)
dri.quit()

for px in prox:
	options = webdriver.ChromeOptions()
	options.add_argument("--start-maximized")
	options.add_argument('--proxy-server=http://%s' % px)

	driver = webdriver.Chrome(pth,options=options)
	url="https://collegedunia.com/courses/arts-courses-after-10th"
	driver.get(url)
	
	
	
	
	