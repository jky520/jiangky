# -*- coding:utf-8 -*-
# Author:@DT人
import json  # alt+enter
import requests
from requests.exceptions import RequestException
import re

def get_one_page(url):
    """获得猫眼单页"""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src=".*?".*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releastime">(.*?)</p>'
                         +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S) # re.S表示可以匹配换行符
    items = re.findall(pattern, html)
    for item in items:
        yield { # 格式化
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5]+item[6]
        }
def write_to_file(content):
    """写入到文件中去"""
    with open('result.txt','a') as f:
        f.write(json.dumps(content + '\n'))
        f.close()

def main():
    url = 'http://maoyan.com/board/4?'
    html = get_one_page(url)
    for item in parse_one_page(html):
        # print(item)
        write_to_file(item)

if __name__ == '__main__':
    main()

