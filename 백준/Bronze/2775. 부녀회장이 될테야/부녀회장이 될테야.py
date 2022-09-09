import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    L = list(range(1,n+2))
    q = 0
    while 1:
        if k == q:
            break
        else:
            q += 1
            for j in range(1,n+1):
                L[j] += L[j-1]
    print(L[n-1]) 