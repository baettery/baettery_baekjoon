import sys
a=b=c=1
while 1:
    a, b, c= map(int,sys.stdin.readline().split())
    if (a==0)&(b==0)&(c==0):
        break
    else:
        list1=[a,b,c]
        list1.sort()
        
        if (list1[2])**2 == ((list1[1])**2 + int(list1[0])**2):
            print('right')
        else:
            print('wrong')