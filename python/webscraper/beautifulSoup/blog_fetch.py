from bs4 import BeautifulSoup

import requests

base_url = "http://www.iwillteachyoutoberich.com/blog/page/"



def grab_url(url):
	r = requests.get(url)
	data = r.text
	soup = BeautifulSoup(data, 'lxml')
	print soup
	# new_article_list = soup.findAll("div", {'class':'article'})
	print soup.findAll("div")
	#for article in new_article_list:
	# return new_article_list



print grab_url("http://www.iwillteachyoutoberich.com/blog/page/234/")

# for i in range(1, 234):
# 	url = base_url + "%d" % (i)
