# -*- coding: utf-8 -*-

# Define your item pipelines here
from .model import Base, engine, loadSession
from .model import zufang


class JiangkyPipeline(object):
    # 搜索Base的所有子类，并在数据库中生成表
    # Base.metadata.create_all(engine)

    def process_item(self, item, spider):
        # print(spider.name,'pipelines') # 打印的是哪个爬虫将数据传到这里
        # insert_sql = "insert into t_zufang(title, money) values('{}','{}')".format(item['title'], item['money'])
        # zf = zufang.Zufang( # 实例化对象
        #     title = item['title'],
        #     money = item['money']
        # )
        # session = loadSession()
        # session.add(zf)
        # session.commit()
        return item