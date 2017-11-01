# -*- coding:utf-8 -*-
# Author:@DT人
import scrapy
from scrapy.http.cookies import CookieJar
from scrapy.selector import Selector

class ChoutiSpider(scrapy.Spider):
    """抽屉爬虫"""
    name = "chouti"  # 给scrapy取名子叫chouti
    allowed_domains = ["chouti.com", ];
    start_urls = ['http://dig.chouti.com/']

    cookie_dict = None
    def parse(self, response):
        print(response)
        cookie_obj = CookieJar()
        cookie_obj.extract_cookies(response, response.request)
        self.cookie_dict = cookie_obj._cookies
        # print(cookie_obj._cookies)  # scrapy crawl jiangky --nolog
        # 用户名密码+cookies
        yield scrapy.Request(
            url="http://dig.chouti.com/login",
            method='POST',
            body="phone=8615285988836&password=jky1988&oneMonth=1",
            headers={'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8"},
            cookies=cookie_obj._cookies,
            callback=self.check_login
        )

    def check_login(self, response):
        # print("==============",response.text)
        # yield scrapy.Request(url="http://dig.chouti.com/", callback=self.good)
        yield scrapy.Request(url="http://dig.chouti.com/", callback=self.good)

    def cancel(self, response):
        """取消点赞"""
        id_list = Selector(response=response).xpath('//div[@share-linkid]/@share-linkid').extract()
        # print(id_list)
        for nid in id_list:
            url = "http://dig.chouti.com/vote/cancel/vote.do?linksId=%s" % nid
            yield scrapy.Request(
                url=url,
                method="POST",
                cookies=self.cookie_dict,
                callback=self.show
            )
        page_urls = Selector(response=response).xpath("//div[@id='dig_lcpage']//a/@href").extract()
        for page in page_urls:
            url = "http://dig.chouti.com%s" % page
            yield scrapy.Request(url=url, callback=self.cancel)


    def good(self, response):
        """点赞"""
        id_list = Selector(response=response).xpath('//div[@share-linkid]/@share-linkid').extract()
        # print(id_list)
        for nid in id_list:
            url = "http://dig.chouti.com/link/vote?linksId=%s" % nid
            yield scrapy.Request(
                url=url,
                method="POST",
                cookies=self.cookie_dict,
                callback=self.show
            )
        page_urls = Selector(response=response).xpath("//div[@id='dig_lcpage']//a/@href").extract()
        for page in page_urls:
            url = "http://dig.chouti.com%s" % page
            yield scrapy.Request(url=url, callback=self.good)

    def show(self,response):
        print(response.text)