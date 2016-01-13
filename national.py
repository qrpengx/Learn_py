#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
proxies = {
  "http": "http://127.0.0.1:1080",
  "https": "http://127.0.0.1:1080",
}
def get_image_url():
	url = "http://photography.nationalgeographic.com/photography/photo-of-the-day"
	htmldoc = requests.get(url, proxies=proxies).text
	soup = BeautifulSoup(htmldoc,'html.parser')
	div = soup.find('div', class_ = 'primary_photo')
	img = div.find('img')['src']
	image_url = "http:" + img
	return	image_url
def download_file(url):
	local_name = url.split('/')[-1]
	response = requests.get(url)
	if response.status_code == 200:
		f = open(local_name, 'wb')
		f.write(response.content)
		f.close()
	else:
		print('Sorry, there is no image today.')
		sys.exit(0)
if __name__ == '__main__':
	image_url = get_image_url()
	print image_url
	download_file(image_url)	