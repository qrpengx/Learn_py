#!/usr/bin/python
# -*- coding: utf-8 -*-
import os,time
import selenium.webdriver.support.ui as ui
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import TimeoutException
filedir = os.path.dirname(__file__)
proxy_file = os.path.join(filedir, "proxy.txt")
proxy_ok_file = os.path.join(filedir, "check.txt")
def openchrome(url, proxy):
	chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--proxy-server=%s' % proxy)
	chrome_options.add_argument('--window-size=800,600')
	chrome_options.add_argument('–incognito')
	driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chrome_options)
	#wait = ui.WebDriverWait(driver,5)
	try:
		driver.get(url)
		#driver.execute_script("window.scrollBy(0,document.body.scrollHeight)","")
		driver.implicitly_wait(10)
		driver.find_element_by_id("kw").send_keys("cyshare.net")
		driver.find_element_by_id("su").click()
		time.sleep(3)
		line_list = driver.find_elements_by_xpath("//h3[@class='t']")
		for line in line_list:
			t = line.find_element_by_xpath("a")
			#print '%s - %s' % (t.text, type(t.text))
			if u"城阳分享论坛 - 城阳,城阳论坛,城阳美食,城阳婚纱摄影" in t.text:
				#print 'yes'
				t.click()
				time.sleep(60)
		#driver.find_element_by_xpath("//a[@href='http://www.cyshare.net/']").click()
	except (TimeoutException, NoSuchElementException, ElementNotVisibleException):
		print '111111'
	finally:
		driver.quit()	
if __name__ == '__main__':
	url = 'http://www.baidu.com/'
	for proxy in open(proxy_ok_file):
		openchrome(url, proxy)