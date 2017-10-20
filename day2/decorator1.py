# -*- coding:utf-8 -*-
# Author:@DT人

import time

# 牛逼的装饰器

user, ps = "jky", "123"

def auth(auth_type):
    print("auth fun:", auth_type)
    def outerwarpper(func):
        def wrapper(*args, **kwargs):
            print("wrapper  func args:", auth_type)
            if auth_type == "local":
                username = input("Username:").strip()
                password = input("Password:").strip()
                if username == user and password == ps:
                    print("\033[32;1mUser has passed authentication\033[0m")
                    rest = func(*args, **kwargs)  # 调用方法
                    print("after authentication")
                    return rest
                else:
                    exit("\033[32;1mInvalid username or password \033[0m")
            elif auth_type == "jky":
                print("做什么呢")
        return wrapper
    return outerwarpper


def index():
    print("welcome to index.html page");

@auth(auth_type="local")
def home():
    print("welcome to home page")
    return "from home"

@auth(auth_type="jky")
def bbs():
    print("welcome to bbs page")


index()
home()
bbs()