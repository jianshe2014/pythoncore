#coding:utf-8
'''
练习变量的定义和命名规则
'''

a=3
b=a
a="hello python"

print a,b
print id(a),id(b)
print type(a),type(b)

##结果显示
#hello python 3
#20146440 19837656
#<type 'str'> <type 'int'>


print 3+5
