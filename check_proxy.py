#!/usr/bin/python
# -*- coding: utf-8 -*-
import os,requests,time
from multiprocessing.dummy import Pool as ThreadPool
url = 'http://27.221.91.9/cacti/ip.php'
headers = {
        'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection' : 'Keep-Alive',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}
timeout = 5

filedir = os.path.dirname(__file__)
proxy_file = os.path.join(filedir, "proxy.txt")
proxy_ok_file = os.path.join(filedir, "check.txt")

def check(http_proxy):
	try:
		http_proxy  = http_proxy
		timeout = 5
		proxy = {
			"http" : http_proxy
			}		
		response = requests.get(url, timeout=timeout, headers=headers, proxies=proxy)
		response.encoding = 'utf-8'
	except requests.exceptions.RequestException:
		print http_proxy + " -- is BAD -- " + "\n"
	else:
		ip1 = response.content
		ip2 = http_proxy.split(":")[0]
		if ip1.replace("\n","") == ip2:
			print http_proxy + " -- is OK -- " + "\n"
		#else:
		#	print ip1.replace("\n","")
		#	print ip2
		#	print http_proxy + " -- is OK -- " + "\n"
			with open(proxy_ok_file, 'a') as file:
				file.write(http_proxy + "\n")
				file.close()
def read_proxy_list(filename):
	listfile = filename
	lists = []
	for line in open(listfile,'r'):
		lists.append(line.replace("\n",""))
	return lists
def main():
	if os.path.exists(proxy_ok_file):
		os.remove(proxy_ok_file)
	pool = ThreadPool(20)
	tstart = time.time()
	pool.map(check,read_proxy_list(proxy_file))
	pool.close()
	pool.join()
	tuse = time.time() - tstart
	print tuse	
if __name__ == '__main__':
	main()