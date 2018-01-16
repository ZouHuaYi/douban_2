# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import sys
reload (sys)
sys.setdefaultencoding('utf8')


import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    city = scrapy.Field()
    timelen = scrapy.Field()
    rate = scrapy.Field()
    year = scrapy.Field()
    type = scrapy.Field()