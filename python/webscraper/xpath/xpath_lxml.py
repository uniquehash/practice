#! /usr/local/bin/python

from lxml import html
import requests

page = requests.get('http://stackoverflow.com/questions?pagesize=50&sort=newest')

tree = html.fromstring(page.content)

questions = tree.xpath('//div[@id="questions"]/*/div[2]/h3/a')

print len(questions)
print questions[0].text