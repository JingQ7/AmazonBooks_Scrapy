# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class AmazonItem(scrapy.Item):
    books_name = scrapy.Field()
    author = scrapy.Field()
    price = scrapy.Field()
    books_link = scrapy.Field()

