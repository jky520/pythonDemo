# -*- coding:utf-8 -*-
# Author:@DT人
import getpass
# 标准库 类似于java 的import
_username="jky";
_password="123456";
username = input("username:");
password = getpass.getpass("password:");

if _username == username and _password == password:
    print("Welcome user {name} login...".format(name=username));
else:
    print("Invalid username or password!")
