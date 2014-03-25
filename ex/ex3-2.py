#coding:utf-8
'''
'''
	
score = raw_input("????????\n")
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
	print "??????"
