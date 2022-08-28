import sys
input = sys.stdin.readline
for i in range(3):
    L = list(map(int,input().split()))
    n = L.count(1)
    if n==4:
        print('E')
    elif n==3:
        print('A')
    elif n==2:
        print('B')
    elif n==1:
        print('C')
    else:
        print('D')