# -*- coding:utf-8 -*-
# Author:@DT人

from lib.aa import C  # 导入lib下面的aa模块的C类

obj  = C()
print(obj.__module__) # 输出 lib.aa,输出模块
print(obj.__class__)  # 输出类的全路劲