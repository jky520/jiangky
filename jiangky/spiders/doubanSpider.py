# -*- coding:utf-8 -*-
# Author:@DT人
import requests
from requests.exceptions import RequestException
import re

def get_one_page(url):
    """获得整个页面"""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def main():
    url = 'https://movie.douban.com/top250'
    html = get_one_page(url)
    print(html)

def paser_one_page(html):
    """转换单页数据"""
    pattern = re.compile('<ol class="grid_view">.*?item')
    items = re.findall(pattern, html)
    print(items)

if __name__ == '__main__':
    main()