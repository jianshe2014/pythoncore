#coding:utf-8
'''
顺序结构演示
判断结构
'''

score = raw_input("请输入成绩\n")
score = int(score)

if score >=90:
	print "A"
elif score >= 80 and score <90:
	if score >85:
		print "B+"
	else:
		print "B"
elif score >=60 and score < 80:
	print "C"
else:
	print "不及格"
	
	