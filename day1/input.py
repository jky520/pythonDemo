# -*- coding:utf-8 -*-
# Author:@DT人
# 用户交互以及格式化
username = input("username:");
age = int(input("age:")); # 强制类型转换
job = input("job:");
salary = input("salary:");

# str(age)
print(type(age));

# %s string, %d int
info = '''
----------info of ------------
Name:%s
Age:%d
Job:%s
Salary:%s
''' % (username, age, job, salary)

info2 = '''
----------info of ------------
Name:{_name}
Age:{_age}
Job:{_job}
Salary:{_salary}
'''.format(_name=username,
           _age=age,
           _job = job,
           _salary = salary);

info3 = '''
----------info of ------------
Name:{0}
Age:{1}
Job:{2}
Salary:{3}
'''.format(username, age,job,salary);

print(info);
print(info2);
print(info3);