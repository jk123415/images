# -*- coding: utf-8 -*-
import scrapy
import time
from CIMGS.items import CimgsItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ImagesdownsSpider(CrawlSpider):
    name = 'idls'
    allowed_domains = ['www.mm131.com']
    start_urls = ['http://www.mm131.com/']

    rules = (
        Rule(LinkExtractor(allow=r'mm131\.com/\w+/', restrict_css=('.nav ul a',)), follow=True),
        Rule(LinkExtractor(allow=r'mm131\.com/\w+/\d+_?\d*\.html'), callback='parse_item',follow=True)
    )

    def parse_item(self, response):
        item = CimgsItem()
        item['page_href'] = response.url
        item['name'] = response.css('h5::text').get()
        item['image_hrefs'] = response.css('.content-pic img::attr(src)').getall()
        item['col_time'] = time.asctime()
        return item
