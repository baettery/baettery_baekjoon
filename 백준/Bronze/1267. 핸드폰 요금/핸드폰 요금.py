import sys
input = sys.stdin.readline
n = int(input())
L = list(map(int,input().split()))
L = list(map(int, L))
#영식
y = 0
for i in range(len(L)):
    y += (L[i]//30+1)*10
#민식
m = 0
for i in range(len(L)):
    m += (L[i]//60+1)*15


if y>m:
    print('M '+str(m))
elif y==m:
    print('Y M '+str(y))
else:
    print('Y '+str(y))
