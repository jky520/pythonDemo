# -*- coding:utf-8 -*-
# Author:@DT人

class Dog(object):
    """Dog类"""

    def __init__(self, name):
        self.name = name;
        self.__food = None # 私有方法

    @property # 属性方法
    def eat(self):
        print("%s is eatting %s " % (self.name,self.__food) )

    @eat.setter
    def eat(self, food):  # 必须重新写这个方法，必须名字一样
        print("set to food:", food)
        self.__food = food # 赋值

    @eat.deleter
    def eat(self):
        del self.__food
        print("删除完了")

d = Dog("jky")
d.eat
d.eat = "包子" # 调用属性方法，把方法当作属性来使用

d.eat

del d.eat # 删除
