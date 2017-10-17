# -*- coding:utf-8 -*-
# Author:@DT人
# if...else if...else
age = 30;

guess_age = int(input("guess age:"));

if guess_age == age :
    print("yes, you get it");
elif guess_age > age:
    print("think smaller...");
else:
    print("think bigger!!")