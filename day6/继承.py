# -*- coding:utf-8 -*-
# Author:@DT人

# class Person:  # 经典类
class Person(object): # 新式类的写法，支持多继承
    '''这是人类'''

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s is eating...." % self.name)

    def talk(self):
        print("%s is talking...." % self.name)

    def sleep(self):
        print("%s is sleeping...." % self.name)

class Relation(object):
    def make_friend(self,obj):
        print("%s is making friends with % s" %(self.name, obj.name))

class Man(Person,Relation): # Man类继承Person类
    '''男人类'''
    def __init__(self,name,age,money):
        # Person.__init__(self, name, age) # 调用父类的构造函数
        super(Man, self).__init__(name, age) # 另外一种调用父类构造函数的方法，新式类的写法
        self.money = money

    def run(self):
        print("%s is running ....20s....done")

class Womam(Person,Relation):
    def get_birth(self):
        print("%s is born a baby...." % self.name)

m = Man("张三",30,100) # 因为父类有两个参数的构造函数
m.eat()

print(Person.__doc__) # 打印类的注视

