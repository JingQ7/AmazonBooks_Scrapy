# -*- coding: utf-8 -*-
import scrapy
from amazon.items import AmazonItem
from scrapy.http import Request


class BooksscrapSpider(scrapy.Spider):
    name = 'booksScrap'
    allowed_domains = ['amazon.ca']
    start_urls = [
        'https://www.amazon.ca/Best-Sellers-Books/zgbs/books/'
        #'https://www.amazon.ca/Best-Sellers-Books/zgbs/books/ref=zg_bs_pg_2?_encoding=UTF8&pg=2'
]

    def parse(self, response):
        book = AmazonItem()
        book['books_name'] = response.xpath('//div[@class="p13n-sc-truncate p13n-sc-line-clamp-1"]/text()').extract()
        book['author'] = response.xpath('//span[@class="a-size-small a-color-base"]/text()').extract()
        book['price'] = response.xpath('//span[@class="p13n-sc-price"]/text()').extract()
        book['books_link'] = response.xpath('//a[@class="a-link-normal a-text-normal"]/@href').extract()
        yield book
        for i in range(1, 2):
            url = 'https://www.amazon.ca/Best-Sellers-Books/zgbs/books/ref=zg_bs_pg_' + str(i) + \
                 '?_encoding=UTF8&pg=' + str(i)
            yield Request(url=url, callback=self.parse)

