# -*- coding:utf-8 -*-
# Author:@DT人

import pymysql

# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='db_python')
# 创建游标
cursor = conn.cursor()

# 执行SQL，并返回收影响行数
effect_row = cursor.execute("select * from t_user")
print(effect_row)
print(cursor.fetchone())
print(cursor.fetchall())

cursor.executemany("insert")
conn.commit()
conn.close()
