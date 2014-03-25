#coding:utf-8

'''
用循环崁套的方式计算连续整数之和，要求输出结果如下。如果输入数5，输出连续5个数字之和：
1 = 1
1+2 = 3
1+2+3 = 6
1+2+3+4 = 10
1+2+3+4+5 = 15
'''

n = int(raw_input("n:\n")) 
a_list = [0]*(n+1)
a_list[0]=0

for i in xrange(1,n+1):
	a_list[i]=a_list[i-1]+i
	
print "连续%d个数之和为%d" %(n,a_list[n])
print a_list
	
	