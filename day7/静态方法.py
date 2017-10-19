# -*- coding:utf-8 -*-
# Author:@DT人

class Dog(object):
    """Dog类"""
    name = "DT"
    def __init__(self, name):
        self.name = name;

    @staticmethod # 静态方法与类没什么关系,只是一个单纯的函数，也是一个装饰器
    def eat(food):
        print("%s is eatting %s " %(food, food))

    @classmethod # 类方法的装饰器,类方法只能访问类变量
    def talk(self):
        print("%s is talking " % self.name)

d = Dog("jky")
Dog.eat("包子")
d.talk()