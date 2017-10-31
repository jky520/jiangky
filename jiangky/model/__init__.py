# -*- coding:utf-8 -*-
# Author:@DT人
# ORM框架sqlalchemy，必须要pip install PyMySQL以及pip install SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 创建对象的基类:
Base = declarative_base()

# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/db_scrapy?charset=utf8', echo = True)

#返回数据库会话
def loadSession():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session