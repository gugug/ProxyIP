# ecoding=utf-8
__author__ = 'gu'
import re

"""
    1. 正则表达式中的三组括号把匹配结果分成三组
    group() 同group（0）就是匹配正则表达式整体结果
    group(1) 列出第一个括号匹配部分，group(2) 列出第二个括号匹配部分，group(3) 列出第三个括号匹配部分。

    2. 没有匹配成功的，re.search（）返回None

    3. 当然正则表达式中没有括号，group(1)肯定不对了。
"""

def testgroup():
    a = "123abc456"
    print re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(0)  # 123abc456,返回整体
    print re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(1)  # 123
    print re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(2)  # abc
    print re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(3)  # 456

testgroup()