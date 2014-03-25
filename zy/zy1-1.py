#coding:utf-8

'''
请写出以下逻辑表达式的值
False and None
0 and None or () and []
True and None or () and []
0 or None and () or []
True or None and () or []
1 or None and 'a' or 'b'
'''

print False and None
print 0 and None or () and []
print True and None or () and []
print 0 or None and () or []
print True or None and () or []
print 1 or None and 'a' or 'b'

#打印结果如下：
False
()
()
[]
True
1