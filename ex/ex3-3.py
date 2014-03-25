#coding:utf-8
'''
循环结构演示
'''

###111
i=0
while i < 10:
	i+=1
	print i,
else :    #这里虽然可以这么用，但是用的很少
	print "\nwhile 完成"

####222
i=0	
while True:
	i+=1
	if i > 10:
		break
	if i == 5:
		continue
	print i,	
	
###333
print "\n"
flag = True
i=0
while flag:
	i+=1
	if i > 10:
		flag = False
	if i == 5:
		continue
	print i,		