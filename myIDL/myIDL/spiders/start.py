# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from myIDL.items import MyidlItem


class StartSpider(CrawlSpider):
    name = 'start'
    allowed_domains = ['www.mm131.com']
    start_urls = ['http://www.mm131.com']

    rules = (
        Rule(LinkExtractor(allow=r'www\.mm131\.com'), callback='parse_item'),
    )

    def __init__(self):
        super().__init__()
        self.referer = 'http://www.mm131.com'

    def parse_item(self, response):
        item = MyidlItem()
        item['name'] = response.css('h5::text').get()
        item['image_urls'] = response.css('.content-pic img::attr(src)').getall()
        item['url'] = response.url
        print(item)
        yield item
