# -*- coding:utf-8 -*-
# Author:@DT人
import scrapy
from scrapy.http.cookies import CookieJar
import selectors

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
        print("==============",response.text)
        yield scrapy.Request(url="http://dig.chouti.com/", callback=self.good)

    def good(self, response):
        # selectors.Selector(response=response).
        pass