#coding:utf-8
'''
�ж�һ�����Ƿ�Ϊ��ȫ�� 
'''
num = int(raw_input("please input num\n:"))
sum = 0
x = 1
while x < num:
 if num % x == 0:
  sum +=x
 x+=1
 
if sum == num:
 print str(num)+"��ȫ��"
else:
 print str(num)+"������ȫ��"

	
