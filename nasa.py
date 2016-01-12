#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
if len(soup.select('img')) > 0:
    img = soup.select('img')[0]
else:
    print('Sorry, there is no image today.')
    sys.exit(0)
"""	
import requests
from bs4 import BeautifulSoup
def get_site_html():
	url = "http://apod.nasa.gov/apod/"
	htmldoc = requests.get(url).text
	soup = BeautifulSoup(htmldoc,'html.parser')
	img_tag = soup.find_all('img')
	image_url = img_tag[0]['src']
	imgurl = 'http://apod.nasa.gov/apod/' + image_url
	return imgurl
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
	text_html = get_site_html()
	download_file(text_html)
