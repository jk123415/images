# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import scrapy


class CimgsItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    image_hrefs = scrapy.Field()
    page_href = scrapy.Field()
    col_time = scrapy.Field()
    image_paths = scrapy.Field()
