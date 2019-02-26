# -*- coding: utf-8 -*-
import scrapy
from imgs.items import ImgsItem


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ["www.mm131.com"]
    start_urls = ['http://www.mm131.com/qingchun/2194.html']

    def parse(self, response):
        item = ImgsItem()
        item['name'] = response.css(".content h5::text").get()
        item['ImgUrl'] = response.css(".content-pic img::attr(src)").getall()
        yield item
        next_url = response.css(".page-ch:last-child::attr(href)").get()
        if next_url is not None:
            pass
            #yield response.follow(next_url, callback=self.parse)