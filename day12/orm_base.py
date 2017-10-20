# -*- coding:utf-8 -*-
# Author:@DT人
import pymysql

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:123456@localhost/db_python",
                       encoding='utf-8', echo=True)

Base = declarative_base() #生成orm基类

class User(Base):
    __tablename__ = 't_user' # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))
    age = Column(Integer)

    def __repr__(self):  # toString()
        return "<id:%s name:%s>" %(self.id, self.name)

Base.metadata.create_all(engine)  # 创建表结构


#========================================添加================================================

Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session_class,需要绑定engine
Session = Session_class() # 生成sessions实例 cusor
#
# user_obj = User(name = "fuguixiansheng", password="123456", age=28)  # 生成你需要的数据对象
# user_obj2 = User(name = "DT", password="123456", age=30)  # 生成你需要的数据对象
#
# Session.add(user_obj) # 把需要的数据对象添加到这个session里，一会儿统一建
# Session.add(user_obj2)
# Session.commit()  # 提交，不然不能插入数据
#======================================查询===================================================
#data = Session.query(User).filter_by().all() # 只能有单等号
data = Session.query(User).filter(User.id>1).all() # filter接收布尔表达式
print(data)

