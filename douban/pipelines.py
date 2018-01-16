# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
reload (sys)
sys.setdefaultencoding('utf-8')
import json
import MySQLdb

class DoubanPipeline(object):
	def __init__(self):
		self.f = open('movie.json','w')
		self.f.write('[')

	def process_item(self, item, spider):
		content = ','+json.dumps(dict(item),ensure_ascii=False)
		#content = unicode.encode(str,'utf-8');
		self.f.write(content)
		return item

	def close_spider(self,spider):
		self.f.write(']')
		self.f.close()	        

