#coding:utf-8
'''
��ֵ��
'''

#��ӡ��ֵ��
print "X     	  y        x and  y    x or q"	
length = len("X     	  y        x and  y    x or q")
#print length *"_"
print "_" * length

for x in [True,False]:
	for y in [True,False]:
		print "%-9s %-9s %-9s %-9s" %(x,y,(x and y),(x or y))
		
		

#��ӡ�������Ϣ		
p = True
q = False

print p and q  #False
print p or q	
#False��qΪ�٣���Or�������δ����

print p or q and q
#True

p1 = True
q1 = False
print p1 and q1  
#False
print p1 or q1
#True

#�������ʽ��һ�㲻��Ҫ�ӣ���
if p and q :
	print  p and q 
else:
	print "ΪFalse"
	



		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
