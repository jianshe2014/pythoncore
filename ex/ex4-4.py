#coding:utf-8
'''
切饼。切法是让2刀的直线都有交叉点。
q(1)=1+1=2
q(2)=1+!+2=4
q(3)=1+1+2+3=7
q(4)=1+1+2+3+4=11
q(n)=q(n-1)+n
q(0) 一刀不切还是一张大饼
'''

a_list = [0]*100
a_list[0] =1

for i in xrange(1,100):
	a_list[i]=a_list[i-1]+i

print a_list
print "100刀后最多切%d块"%a_list[99]
	