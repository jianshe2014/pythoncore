#coding:utf-8

'''
用键盘输入15以内的整数，输出这样的格式。
            1 
          2 1 2 
        3 2 1 2 3 
      4 3 2 1 2 3 4 
    5 4 3 2 1 2 3 4 5 
  6 5 4 3 2 1 2 3 4 5 6 
7 6 5 4 3 2 1 2 3 4 5 6 7 
'''

#未考虑前排空格的情况
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

#考虑前排空格的情况
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

