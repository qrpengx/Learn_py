# -*- coding: utf-8 -*-
import os
import re
import time
import requests
import lxml.html
import selenium.webdriver.support.ui as ui
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from multiprocessing.dummy import Pool as ThreadPool

filedir = os.path.dirname(__file__)
proxy_file = os.path.join(filedir, "proxy.txt")

#proxy = '127.0.0.1:8787'
headers = { 'User-agent', 'Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0' }
proxies = {
  "http": "http://127.0.0.1:8787"
}
def get_cn_proxy_list():
    print '=> get cn-proxy.com'
    req = requests.get("http://cn-proxy.com/", proxies=proxies)
    soup = BeautifulSoup(req.text, "html.parser")
    contents = soup.find_all('tr')
    regex = re.compile('\d+')
    for each in contents:
        sock = each.find_all('td')
        if sock:
            ip = sock[0].text
            port = sock[1].text
            if re.findall(regex, ip):
                proxy = '%s:%s\n' %(ip, port)
		with open(proxy_file,"a+") as fd:
			fd.write(proxy)
			fd.close
def get_kuaidaili_list():
    for i in range(1, 11):
		url = "http://www.kuaidaili.com/proxylist/%s/" % i
		chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument('--window-size=40,40')
		driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chrome_options)
		driver.get(url)
		text = driver.page_source.encode('utf-8')
		driver.quit()
		soup = BeautifulSoup(text, "html.parser")
		contents = soup.find_all('tr')
		regex = re.compile('\d+')
		for each in contents:
			sock = each.find_all('td')
			if sock:
				ip = sock[0].text
				port = sock[1].text
				if re.findall(regex, ip):
					proxy = '%s:%s\n' %(ip, port)
					with open(proxy_file,"a+") as fd:
						fd.write(proxy)
						fd.close
def openchrome(url, proxy):
	chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--proxy-server=%s' % proxy)
	chrome_options.add_argument('--window-size=40,40')
	driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chrome_options)
	wait = ui.WebDriverWait(driver,10)
	try:
		driver.get(url)
	except TimeoutException:
		print '111111'
	finally:
		driver.quit()

if __name__ == '__main__':
	url = 'http://www.cyshare.net'
	get_kuaidaili_list()
	get_cn_proxy_list()
	for proxy in open(proxy_file):
		openchrome(url, proxy)