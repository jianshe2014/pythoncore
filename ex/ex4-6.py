#coding:utf-8
'''
要求whlle循环和print语句
打印
1
1	2
1	2	3
1	2	3	4
1	2	3	4	5
1	2	3	4	5	6

'''

num = int(raw_input("num:\n"))
i = 1

while i < num:
	i += 1
	j = 1
	while j < i:
		print j,
		j +=1
	print	