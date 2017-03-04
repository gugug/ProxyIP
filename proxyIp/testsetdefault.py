# coding=utf-8
__author__ = 'gu'
"""
setdefault()方法语法：
    dict.setdefault(key, default=None)

参数
    key -- 查找的键值。
    default -- 键不存在时，设置的默认键值。

返回值
    该方法没有任何返回值。
"""

def testsetdefault():

    dict = {'Name': 'Zara', 'Age': 7}

    print "Value : %s" % dict.setdefault('Age', None)
    print "Value : %s" % dict.setdefault('Sex', None)
    print dict.keys()
    for key in dict.keys():
        print key
    print dict.values()

testsetdefault()