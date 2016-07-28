#!/usr/local/bin/python


from pymongo import MongoClient
from bs4 import BeautifulSoup
import requests
import string
from datetime import datetime


client = MongoClient('mongodb://frockhub:frockhub@candidate.49.mongolayer.com:10677,candidate.50.mongolayer.com:10275/frockhub2?replicaSet=set-55e4cc0d87b944a0fa000fc1')
db = client.frockhub2
product = db.products

#strips the non numeric characters from its input
def strip_alpha (alpha_num):
 	clean_id = "";
 	if type (alpha_num) is list:
 		for c in alpha_num[0]:
 			if c.isdigit(): 				
 				clean_id = clean_id + c

 	if type (alpha_num) is unicode:
		for c in alpha_num:
 			if c.isdigit(): 				
 				clean_id = clean_id + c

 	return clean_id	

#cleaning filter for bloomingdales
def ftr_url (substring):
	if 'ID' in substring:
		return substring

#function to print all the items of an iterable
def print_items(items):
	for document in items:
		print "name: ", document['name']
		print "brand: ", document['brand']
		print "url: ", document['url']
		print "gender: ", document['gender']
		print "---------------------"	

		

#find a sku by url targeted towards bloomingdales
def clean_url(document):
	mongo_id = document['_id']
	name = document['name']
	url = document['url']
	split_url = url.split("?")
	dirty_sku = filter(ftr_url, split_url)
	clean_sku_ID = strip_alpha(dirty_sku)
	return (mongo_id, name, clean_sku_ID)

#find a sku by url targeted towards barneys
def clean_url_barneys(document):
	mongo_id = document['_id']
	name = document['name']
	url = document['url']
	split_url = url.split("-")
	clean_sku_ID = strip_alpha(split_url[-1])	
	return (mongo_id, name, clean_sku_ID)

#find a sku by description targeted towards barneys format
def clean_description_barneys(document):
	mongo_id = document['_id']
	name = document['name']
	description = document['description']
	split_description = description.split("Style # ")
	clean_sku_ID = split_description[1]
	return (mongo_id, name, clean_sku_ID)	

#cleans the sku grabed from the scrape. targeted towards neimenmarcus
def grab_url_nm(url):
	r = requests.get(url)
	data = r.text
	soup = BeautifulSoup(data, 'lxml')
	try :
		dirty_sku = soup.findAll("p", {'class':'product-sku OneLinkNoTx'})[0]
	except IndexError:
		dirty_sku = "DeadLink"

	return dirty_sku

def grab_sku_nm(dirty_sku):
	quarter_sku = str(dirty_sku).split(': ')
	half_sku = quarter_sku[-1]
	clean_sku = half_sku.split("</")[0]
	return clean_sku
	
def fetch_sku_nm(document):
	mongo_id = document['_id']
	name = document['name']	
	url = document['url']	
	clean_sku_ID = grab_sku_nm(grab_url_nm(url))	
	return (mongo_id, name, clean_sku_ID)
	

#{"$or": [{"cuisine": "Italian"}, {"address.zipcode": "10075"}]
#items_updated = product.find({"$or":[{"store_name":"barneys"}, {"store_name":"bloomingdales"}]}).count()
#items_investigated = product.find({"$or":[{"store_name":"barneys"}, {"store_name":"bloomingdales"},{"store_name":"bergdorfgoodman"}]}).count()
#other_items = product.find({"store_name": { "$nin": ["bloomingdales","barneys","bergdorfgoodman"]}}).count()

start = datetime.now()
num_request = 80


print "update start: ", start
print "frock2"

female = 0
brands = 0
number = 0 
indexRange = 0
urlRange = [""]
brands_marked_clear = 0

items = product.find({ "$and":[ {"store_name":"neimanmarcus"}, {"sku_id": {"$ne": "DeadLink"}}, {"brand":""}]}).limit(num_request).skip(1000)
print items[0]['name']
"""
for z in items:
	print "number: ", number
	print z['url']
	r = requests.get(z['url'])
	data = r.text
	soup = BeautifulSoup(data, 'lxml')

	p = str(soup.findAll("h6", {"class": "product-name"})[0])
	if "id=" in p:
		brands = brands +1
		a = p.split('id=')[1]
		b = a.split('>')[1]
		c = b.split('<')[0]
		print "brand: ", c
	number = number +1

	#print p
	print "------------------------"

print "num brands found: ", brands
"""

for z in items:
	number = number +1
	#print z['url']
	r = requests.get(z['url'])
	data = r.text
	soup = BeautifulSoup(data, 'lxml')
	"""
	try :
		brand = str(soup.findAll("div", {"class":"aboutDesignerCopy"})[0])
		y = brand.split(">")
		a = y[2].split(":")
		c = a[0].split("About ")[1]
		c = c.lower()
		#product.update_one({"_id":z['_id']}, {"$set":{"brand":c}})
		brands= brands +1
	except IndexError:
		#c = 'no brand'
	"""
	try:
		p = str(soup.findAll("h6", {"class": "product-name"})[0])
		if "id=" in p:
			brands = brands +1
			a = p.split('id=')[1]
			b = a.split('>')[1]
			c = b.split('<')[0]
			product.update_one({"_id":z['_id']}, {"$set":{"brand":c}})
		else:
			brands_marked_clear = brands_marked_clear +1
			product.update_one({"_id":z['_id']}, {"$set":{"brand":0 }})
	except IndexError:
		print "out of range", z['url']
		urlRange.append(z['url'])
		indexRange = indexRange +1
		product.update_one({"_id":z['_id']}, {"$set":{"sku_id":"DeadLink"}})


	try :
		gender = str(soup.findAll("div", {"class":"productCutline"})[0])
		if "dress size US" in gender:
		#	print "female gender:", "dress size" in gender
			product.update_one({"_id":z['_id']}, {"$set":{"gender":"female"}})
			female = female +1
		else:
			pass
		#	print "unsure if female"
	except IndexError:
		#print "can't find productCutline"
		pass
	
finish = datetime.now()
delta = (finish - start).seconds/60.00
print ""
print "------------- data gathered -------------"
print "num brands found: ", brands
print "num female found: ", female
print "num of clear brands", brands_marked_clear
print "num out of range index", indexRange
print ""
print "------------- meta data gathered -------------"
print "number of request: ", num_request 
print "update finished: ", finish
print "time differential: ", delta, "minutes"
print "rough requtest rate: ", num_request/delta, "per minute"
print ""
print "------------- dead links -------------"
print "list of url out of range", urlRange
print ""
print "---------------------------"
print ""








#not relevant

#print gender
#print "dress size" in gender

#print x

#items = product.find({"url":"http://www.neimanmarcus.com/zh-cn/Donna-Karan-Organza-Elbow-Sleeve-Top-Street-Art-Printed-Pleated-Skirt-Hand-Painted-Leather-Belt/prod176660020/p.prod"})

#items = product.find({"brand":"burberry"}).count()

#print_items(items)

#print "items investigated: ", items_investigated
#print "items updated: ", items_updated
#print "remaining items: ", other_items

#print "items being assesed: ", items
#print "diff: ", other_items - items
#edit_list = map(fetch_sku_nm, items)
#print_items(edit_list)

#i = 1
"""
for document in edit_list:	
	#print "entry number: "+str(i)
	product.update_one({"_id":document[0]}, {"$set":{"sku_id":document[2]}})
	#print document
	#print "----------------------------"
	#print ""
	i = i + 1
#shfgjslfg
items_updated_nm = product.find({ "$and":[ {"store_name":"neimanmarcus"}, {"sku_id": {"$exists": True} }]}).count()

print "total NM items updated so far: ", items_updated_nm
print "update finished: ", datetime.now().time()
"""




