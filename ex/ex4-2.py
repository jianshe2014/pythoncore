#coding:utf-8
'''
编程思路练习
判断一个数是否为完全数
'''

num = int(raw_input("please input num\n:"))
sum = 0
x = 1
while x < num:
	if num % x == 0:
		sum +=x
	x+=1
	
if sum == num:
	print str(num)+"完全数"
else:
	print str(num)+"不是完全数"
	