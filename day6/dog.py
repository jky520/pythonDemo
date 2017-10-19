# -*- coding:utf-8 -*-
# Author:@DT人

# 析构函数：在实例释放、销毁的时候执行的，通常用于做一些收尾工作，如关闭一些数据库连接，打开的临时文件等等
class Dog:
    n = 1; # 类变量
    name = "类变量的name" # 当实力变量与类变量同时存在，先使用实例变量，再使用类变量

    def __init__(self,name):   # 构造函数类似于，一个参数的构造函数
        self.name = name; # this.name = name

    def __del__(self):  # 析构函数,类似Java的GC
        print("%s 彻底死了。。。。" % self.name)

    def bulk(self):
        print("%s: wang wang wang!" % self.name)

d1 = Dog("黑小狗")  # 实例化对象
d2 = Dog("红小狗")
d3 = Dog("百小狗")
d4 = Dog("旅小狗")

d1.bulk()
d2.bulk()
d3.bulk()
d4.bulk()
