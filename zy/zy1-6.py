#coding:utf-8

'''
�ü�������15���ڵ���������������ĸ�ʽ��
            1 
          2 1 2 
        3 2 1 2 3 
      4 3 2 1 2 3 4 
    5 4 3 2 1 2 3 4 5 
  6 5 4 3 2 1 2 3 4 5 6 
7 6 5 4 3 2 1 2 3 4 5 6 7 
'''

#δ����ǰ�ſո�����
'''
num=int(raw_input("please input num:\n"))
i=1

while i<=num :	
	j=i
	while j:                
		print j,
		j-=1
	j=2
	while j<=i:
		print j,
		j+=1
	i+=1
	print
'''

#����ǰ�ſո�����
num=int(raw_input("please input num:\n"))
i=1
while i<=num:
    i+=1
    j=1
    while j<= num+1-i:
        print " ",
        j+=1
    j=i-1
    while j>=1:
        print j,
        j-=1
    j=1
    while j<i-1:
        j+=1
        print j,     
    print 	

