#coding:utf-8

'''
ֻ����while��print�����������ͼ��
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
#��ӡ�ϰ벿��    
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
#��ӡ�°벿��
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
        


        

