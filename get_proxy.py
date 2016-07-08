# -*- coding: utf-8 -*-
import os
import re
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

filedir = os.path.dirname(__file__)
proxy_file = os.path.join(filedir, "proxy.txt")
proxy_ok_file = os.path.join(filedir, "check.txt")

#proxy = '127.0.0.1:8787'
headers = {
        'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection' : 'Keep-Alive',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}
timeout = 5
proxies = {
  "http": "http://127.0.0.1:8787"
}
def wproxyfile(proxy):
	with open(proxy_file,"a+") as fd:
		fd.write(proxy)
		fd.close
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
		wproxyfile(proxy)
def get_kuaidaili_list():
    for i in range(1, 11):
		url = "http://www.kuaidaili.com/proxylist/%s/" % i
		chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument('--window-size=40,40')
		driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chrome_options)
		driver.get(url)
		time.sleep(3)
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
					wproxyfile(proxy)
def get_ip84_list():
	URLS = ['http://ip84.com/dlgn-http/{0}'.format(i) for i in range(1, 11)]
	for url in URLS:
		req = requests.get(url)
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
					wproxyfile(proxy)
def get_xici():
	URLS = ['http://www.xicidaili.com/nn/{0}'.format(i) for i in range(1, 6)]
	for url in URLS:
		req = requests.get(url, headers=headers)
		soup = BeautifulSoup(req.text, "html.parser")
		trs = soup.find('table', id='ip_list').find_all('tr')
		for tr in trs[1:]:
			tds = tr.find_all('td')
			ip = tds[1].text.strip()
			port = tds[2].text.strip()
			proxy = '%s:%s\n' %(ip, port)
			#protocol = tds[5].text.strip()
			wproxyfile(proxy)
if __name__ == '__main__':
	get_ip84_list()
	get_cn_proxy_list()
	get_kuaidaili_list()
	get_xici()