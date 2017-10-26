# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JiangkyItem(scrapy.Item):
    """从爬虫中把数据传到项目管道文件中，必须通item创建一个类才能传过去"""
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    money = scrapy.Field()
    # pass
