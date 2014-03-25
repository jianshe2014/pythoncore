#coding:utf-8
'''
解释"is "和"= ="之间的差异，示例说明,对is 返回为假，= = 返回为真
'''

'''
Python中的对象包含三要素：id、type、value
其中id用来唯一标识一个对象，type标识对象的类型，value是对象的值
is判断的是a对象是否就是b对象，是通过id来判断的
==判断的是a对象的值是否和b对象的值相等，是通过value来判断的
'''

a=1
b=1.0
print a is b  #输出结果为假
print a==b	#输出结果为真

