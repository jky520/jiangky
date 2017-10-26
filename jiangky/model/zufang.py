# -*- coding:utf-8 -*-
# Author:@DT人
# 数据库表t_zufang的映射文件
from sqlalchemy import Column,String,Integer,DateTime

from . import Base
import datetime
class Zufang(Base):
    """租房实体类"""
    __tablename__ = 't_zufang' # 表名

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=True)
    money = Column(Integer, nullable=False)
    create_at = Column(DateTime,nullable=True)

    def __init__(self,title=None, money=0):
        self.title = title
        self.money = money
        self.create_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")