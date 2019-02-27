# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import re
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
from scrapy.exceptions import DropItem


class CimgsPipeline(object):
    def process_item(self, item, spider):
        return item


class MyImagesDownPipline(ImagesPipeline):

    def get_media_requests(self, item ,info):
        return [Request(x,headers={'referer':'http://www.mm131.com'},meta={'item':item}) for x in item.get('image_hrefs')]

    def file_path(self, request, response=None, info=None):
        name = request.meta['item'].get('name')
        name = re.sub(r'[？\\*|“<>:/()0123456789]', '', name)
        image_guid = request.url.split('/')[-1]
        filename = u'full/{0}/{1}'.format(name, image_guid)
        return filename

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            raise DropItem('Item contains no images')
        item['image_paths'] = image_path
        return item


class MyUserAgent(object):

    def open_spider(self, spider):
        with open('user_agents', encoding='utf-8') as f:
            all_user_agents = f.read().splitlines()
            phone_index = all_user_agents.index('#phone')
            spider.pc_user_agents = all_user_agents[0:phone_index]
            spider.phone_user_agents = all_user_agents[phone_index + 1:]
            all_user_agents.remove('#phone')
            spider.all_user_agents = all_user_agents
