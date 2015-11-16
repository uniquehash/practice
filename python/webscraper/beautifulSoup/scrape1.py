from bs4 import BeautifulSoup

import requests

url = "http://www.neimanmarcus.com/Sweet-Dreams-Primrose-Bedding/prod180920045/p.prod"

def grab_url(url):
	r = requests.get(url)
	data = r.text
	soup = BeautifulSoup(data, 'lxml')
	dirty_sku = soup.findAll("p", {'class':'product-sku OneLinkNoTx'})[0]
	return dirty_sku

def grab_sku_nm(dirty_sku):
	quarter_sku = str(dirty_sku).split(': ')
	half_sku = quarter_sku[-1]
	clean_sku = half_sku.split("</")[0]
	return clean_sku

#r = requests.get(url)
#data = r.text
#soup = BeautifulSoup(data, 'lxml')
#dirty_sku = soup.findAll("p", {'class':'product-sku OneLinkNoTx'})
#clean_sku_ID = dirty_sku['catalog-item']

print grab_sku_nm(grab_url(url))


