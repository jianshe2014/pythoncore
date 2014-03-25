#coding:utf-8

以下的代码x=4时会发生什么情况？
while True :
    for x in range(6):
        y = 2*x + 1
        print y
		if y>9 :
			break
'''

说明：当x=4时，y=9,继续进行下一循环。
