#coding:utf-8
'''
����
����һ���������������������ԣ����������
'''
import random
import string
num = random.randint(0,100)
print num

while True:
 guess = raw_input("please input guess\n:") #�õ������ַ���
 
if guess.isdigit():
 
  if int(guess) == num: #���ʱ��������������
   print "�����"
   break
  elif guess > num:
   print "�������ֵ�ϴ�"
  else:
   print "�������ֵ��С"
 
else:
  print "����������ַ���������������"

	
