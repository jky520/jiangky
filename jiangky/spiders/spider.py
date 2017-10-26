# -*- coding:utf-8 -*-
# Author:@DT人
import scrapy
from ..items import JiangkyItem # 在爬虫文件中导入item

# * 爬虫只负责对网页进行分析并获得数据，管道文件负责对数据清理并且把数据插入到数据库中

class ganjiSpider(scrapy.Spider):
    """赶集网爬虫类"""
    name = "jiangky" # 给scrapy取名子叫jiangky
    start_urls = ['http://gy.ganji.com/fang1/guiyang/'] # 请求路径列表，可以存放多个，它自己会遍历

    def parse(self, response):
        print(response)
        jky = JiangkyItem()
        # 标题列表
        title_list = response.xpath(".//div[@class='f-list-item ershoufang-list']/dl/dd[1]/a/text()").extract()
        # 租金列表
        money_list = response.xpath(".//div[@class='f-list-item ershoufang-list']/dl/dd[5]/div[1]/span[1]/text()").extract()
        for i, j in zip(title_list, money_list): # 把两个列表合并成一个元组，以少的为准
            jky['title'] = i
            jky['money'] = j
            yield jky  # 这样的话，租房item就成功传到pipeline里面
            # print(i, ":", j)