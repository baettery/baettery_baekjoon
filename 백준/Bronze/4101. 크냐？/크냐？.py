import sys
while 1:
    a,b = map(int,sys.stdin.readline().split())
    if (a==0)&(b==0):
        break
    else:
        if a>b:
            print('Yes')
        else:
            print('No')    