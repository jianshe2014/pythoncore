#coding:utf-8

'''
��ѭ�����׵ķ�ʽ������������֮�ͣ�Ҫ�����������¡����������5���������5������֮�ͣ�
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
	
print "����%d����֮��Ϊ%d" %(n,a_list[n])
print a_list
	
	