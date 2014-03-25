#coding:utf-8
'''
运算符
'''

print 18/5
#3
print float(18)/5
#3.6
print 18/float(5)
#3.6
print 18/5.0
#3.6
print 18%5
#3

#强制类型转换
a=9
print float(9)
#9.0

print "hello"+str(3)
#hello3

print bool(3)
#True
'''
while 3:
	a=8
	b=90
	if a>9:
		print a
'''
#多重赋值		
x=1
x=x+1
x+=1
x-=1
x=y=z=1	
print x,y,z
#三个1

#多然赋值
x,y,z=1,2,"hello"
print x,y,z
#1 2 hello

#交换两个变量方法
x = 9
y = 89
x,y = y,x
print "x=%d,y=%d" %(x,y)
#x=89,y=9




