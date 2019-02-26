# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem


class UserAgent(object):
    def open_spider(self, spider):
        with open('D:/images/images/images/user_agents', encoding='utf-8') as f:
            all_user_agents = f.read().splitlines()
            phone_index = all_user_agents.index('#phone')
            spider.pc_user_agents = all_user_agents[0:phone_index]
            spider.phone_user_agents = all_user_agents[phone_index + 1:]
            all_user_agents.remove('#phone')
            spider.all_user_agents = all_user_agents


class ImagesPipeline(object):
    def process_item(self, item, spider):
        return item

class MyImagesDown(ImagesPipeline):
    """docstring for MyImagesDown"""
    def __init__(self):
        pass

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item ,info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('Item contains no images')
        item['image_paths'] = image_paths
        return item


if __name__ == '__main__':
    pass