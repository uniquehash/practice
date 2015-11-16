from scrapy import Spider
from scrapy.selector import Selector
from stack.items import StackItem


class StackSpider(Spider):
	name = "spider_stack"
	allowed_domains = ['stackoverflow.com']
	start_urls = ['http://stackoverflow.com/questions?pagesize=50&sort=newest',]

	def parse(self, response):
		questions = Selector(response)['a']






		return questions
		