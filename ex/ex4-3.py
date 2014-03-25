#coding:utf-8
'''
猜数
输入一个数，如果两个数相等则答对，否则继续猜
'''
import random
import string
num = random.randint(0,100)
print num

while True:
 guess = raw_input("please input guess\n:") #得到的是字符串
 
if guess.isdigit():
 
  if int(guess) == num: #相比时，两侧需是数字
   print "答对了"
   break
  elif guess > num:
   print "输入的数值较大"
  else:
   print "输入的数值较小"
 
else:
  print "你输入的是字符串，请输入数字"

	
