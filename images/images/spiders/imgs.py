# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from images.items import ImagesItem


class ImgsSpider(scrapy.Spider):
    name = 'imgs'
    allowed_domains = ['www.mm131.com']
    start_urls = ['http://www.mm131.com/qingchun/2124.html']
    '''
    rules = (
        #Rule(LinkExtractor(restrict_css='.content-pic img', attrs=('src',)), callback='parse_item'),
        Rule(LinkExtractor(restrict_css='a.page-ch'), callback='parse_item'),
    )
    '''

    def __init__(self):
        self.referer = 'http://www.mm131.com'

    def parse(self, response):
        item = ImagesItem()
        item['url'] = response.url
        item['title'] = response.css('h5::text').get()
        item['image_urls'] = response.css('.content-pic img::attr(src)').getall()
        return item
