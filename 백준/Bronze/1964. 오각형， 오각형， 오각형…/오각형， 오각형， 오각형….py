import sys
n = int(sys.stdin.readline())
k = 0
if n==1:
    k=0
else:
    for i in range(1,n):
        k += 2*i+1

print(int(((n*(n+1)/2)*5-k)%45678))