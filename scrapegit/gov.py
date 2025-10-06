from selenium import webdriver
import docx
import openpyxl
import time

#start PhantomJS
#service_args = [ '--proxy=localhost:9150', '--proxy-type=socks5', ]
#driver = webdriver.PhantomJS(service_args=service_args)
driver = webdriver.Chrome(r'/usr/local/bin/chromedriver')
#alli = ['s', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#doc = docx.Document()

xl = openpyxl.Workbook()
sh = xl.active

i = 1
k = 1
for ix in range(1,500):
	driver.get('http://educationportal.mp.gov.in/Public/Search/Search_DDO.aspx')
	
	print '(=)(=)(=)    Site fetched'

	sl = driver.find_element_by_id('ctl00_ctl00_RMCPH_ContentPlaceHolder1_ddlDistrict')
	bt = driver.find_element_by_id('ctl00_ctl00_RMCPH_ContentPlaceHolder1_btn_Search')
	
	op = sl.find_elements_by_tag_name('option')
	oq = iter(op)
	ot = next(oq)
	
	for om in range(1, k+1):	
		ot = next(oq)
	ot.click()
	dil = {}
	dil[i] = ot.text
	bt.click()

	time.sleep(1)

	tb = driver.find_element_by_id('ctl00_ctl00_RMCPH_ContentPlaceHolder1_GVPADistrict')
	
	
	tr = tb.find_elements_by_tag_name('tr')
	ltr = len(tr)
	print '(+)(+)(+)   '
	if i == ltr:
		print '(+)(+)(+)   Limit Reached'
		k += 1
		
	trr = iter(tr)
	trx = next(trr)
	for trt in range(1, i+1):
		trx = next(trr)
		
	hr = trx.find_element_by_tag_name('a')
	print '(+)(+)(+)   '+hr.text
	
	hr.click()
	time.sleep(1)
	zt = driver.find_element_by_id('ctl00_ctl00_RMCPH_ContentPlaceHolder1_RbtnEmployees')
	zt.click()
	time.sleep(1)
	
	try:
		tbb = driver.find_element_by_id('ctl00_ctl00_RMCPH_ContentPlaceHolder1_GridView1')

		tbr = tbb.find_elements_by_tag_name('tr')
		r1 = 1
		print '(+)(+)(+)   Printing rows'
		for tbx in tbr:
			try:
				td = tbx.find_elements_by_tag_name('td')
			except:
				td = tbx.find_elements_by_tag_name('th')

			r2 = 1
			for tx in td:	
				sh.cell(row = r1, column = r2).value = tx.text
				r2 += 1
			r1 += 1

		xl.save(dil[i]+str(i)+'.xlsx')
		print '(=)(=)(=)     File Saved'
	except:
		pass
	i += 1
	
	
	
	
	



