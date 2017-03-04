# encoding:utf-8
__author__ = 'gu'
a = "[[1,2], [3,4], [5,6], [7,8], [9,0]]"

b = eval(a)  # eval()函数十分强大，官方demo解释为：将字符串str当成有效的表达式来求值并返回计算结果
print "a", type(a)
print "b", type(b)



c = "{1: 'a', 2: 'b'}"

d = eval(c)

print "c", type(c)
print "d", type(d)