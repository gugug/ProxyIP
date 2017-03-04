# coding=utf-8
__author__ = 'gu'
import re

"""
match ：只从字符串的开始与正则表达式匹配，匹配成功返回matchobject，否则返回none；
search ：将字符串的所有字串尝试与正则表达式匹配，如果所有的字串都没有匹配成功，返回none，
否则返回matchobject；（re.search相当于perl中的默认行为）

"""


def testsearchandmatch():
    s1 = "helloworld, i am 30 !"
    w1 = "world"
    m1 = re.search(w1, s1)  # 从字符串开始直到找到与正则表达式匹配的子符合

    if m1:
        print m1.group()  # 返回整体
        print("find : %s" % m1.group())

    if re.match(w1, s1) is None:  # 从头开始匹配字符串
        print re.match(w1, s1)
        print("cannot match")

        w2 = "helloworld"
        m2 = re.match(w2, s1)
    if m2:
        print("match : %s" % m2.group())


testsearchandmatch()
