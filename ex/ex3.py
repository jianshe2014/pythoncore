#coding:utf-8
'''
真值表
'''

#打印真值表
print "X     	  y        x and  y    x or q"	
length = len("X     	  y        x and  y    x or q")
#print length *"_"
print "_" * length

for x in [True,False]:
	for y in [True,False]:
		print "%-9s %-9s %-9s %-9s" %(x,y,(x and y),(x or y))
		
		

#打印具体的信息		
p = True
q = False

print p and q  #False
print p or q	
#False，q为假，则Or会后运算未计算

print p or q and q
#True

p1 = True
q1 = False
print p1 and q1  
#False
print p1 or q1
#True

#条件表达式里一般不需要加（）
if p and q :
	print  p and q 
else:
	print "为False"
	



		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
