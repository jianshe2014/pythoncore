#coding:utf-8

'''
只能用while和print语句输出下面的图样
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''

num=int(raw_input("please input num:\n"))
#打印上半部分    
i=1
while i<=num :    
    j=1
    while j<=num-i:
        print " ",
        j+=1
    j=1
    while j<=2*i-1:
        print "*",
        j+=1
    i+=1
    print 
#打印下半部分
i=1
while i<num :    
    j=1
    while j<=2*num-i-1:
        if j>i:
            print "*",
        else:
            print " ",
        j+=1
    i+=1    
    print 
        


        

