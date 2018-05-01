#! /usr/local/bin/python

from lxml import html
import requests
import time

header = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'en-US,en;q=0.5',
	'Cache-Control': 'max-age=0',
	'Connection': 'keep-alive',	
	'Host': 'burningman.org',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
}


def writeList(file, items, mode):
	with open(file, mode) as f:
		for item in items:
			unicode_safe = item.encode('utf8','replace')
			f.write(unicode_safe + '\n')

def scrapeThemeCamps(header):
	years = ['2015', '2016', '2017']
	alphas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	sleeper = 15
	for year in years:
		for alpha in alphas:
			names = []
			desc = []
			link = 'https://burningman.org/culture/history/brc-history/theme-camp-archive/?ix='+alpha+'&yyyy='+year		
			print year + ': ' + alpha 
			print 'hitting: ' + link
			page = requests.get(link, headers=header)
			tree = html.fromstring(page.content)
			items = tree.xpath("//div[@class='newitem-content']")
			for item in items:			
				names.append(item.getchildren()[0].getchildren()[0].text_content())
				if len(item.getchildren()) > 2:
					desc.append(item.getchildren()[2].text_content().replace('\n', ' '))
				else:
					desc.append('no descriptions')
			writeList('/tmp/names/' + year, names, 'a')
			writeList('/tmp/desc/' + year, desc, 'a')
			print 'sleeping for '+str(sleeper)+'....\n'
			time.sleep(sleeper)



def scrapeArtPieces(header):
	years = ['2014', '2015', '2016', '2017']
	# years = ['2013']
	sleeper = 15
	for year in years:
		names = []
		link = "https://burningman.org/culture/history/brc-history/event-archives/" + year + "-event-archive/" + year + "-art-installations/"
		print year + ' => hitting: ' + link
		page = requests.get(link, headers=header)
		tree = html.fromstring(page.content)
		items = tree.xpath("//div[@class='newitem-content container']")
		for item in items:
			names.append(item.getchildren()[0].getchildren()[0].text_content())
		writeList('/tmp/names/art_' + year, names, 'a')
		print 'sleeping for '+str(sleeper)+'....\n'
		time.sleep(sleeper)
	print 'completed'





scrapeArtPieces(header)
























