# -*- coding:utf-8 -*-
# Author:@DT人

import time
""""
装饰器：本质就是一个函数。
原则：1、不能修改被修饰的函数的函数源码；类似于java的接口与实现类中的实现类
      2、不能修改被装饰的函数的调用方式
      

实现装饰器的知识储备：
    1、函数即是“变量”
    2、
      """

def timmer(func): # 装饰器的定义
    def warpper(*args, **kwargs):
        start_time=time.time()
        func()
        stop_time=time.time()
        print('the func run time is %s' %(stop_time-start_time))
    return warpper

@timmer
def test():
    time.sleep(3);
    print("in the test");

test();