#coding:utf-8

'''
只能用while和print语句输出下面的图样
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
'''

num=int(raw_input("please input num:\n"))
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
        


        

