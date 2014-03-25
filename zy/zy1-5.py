#coding:utf-8

'''
限定用while 循环和print语句输出以下样式
样式1：
1
1 2
1 2 3
1 2 3 4 
1 2 3 4 5
1 2 3 4 5 6 
样式2：
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
样式3：
		  1 
        2 1 
      3 2 1 
    4 3 2 1 
  5 4 3 2 1 
6 5 4 3 2 1  
'''

#样式1
num=int(raw_input("please input num:\n"))
i=1
while i<num :
	i+=1
	j=1
	while j<=i:
		print j,
		j+=1
	print

#样式2
num=int(raw_input("please input num:\n"))
i=1
while i<=num:
	i+=1
	j=1
	while j <=num+2-i:
		print j,
		j+=1
	print

#样式3
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
    print   