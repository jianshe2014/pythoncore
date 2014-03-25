#coding:utf-8
'''
q(1)=1+1=2
q(2)=1+!+2=4
q(3)=1+1+2+3=7
q(4)=1+1+2+3+4=11
q(n)=q(n-1)+n
q(0) 
'''

a_list = [0]*100
a_list[0] =1

for i in xrange(1,100):
	a_list[i]=a_list[i-1]+i

print a_list
print "%d"%a_list[99]


	
