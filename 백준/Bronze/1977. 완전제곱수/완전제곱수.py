import sys
from math import ceil, floor
input = sys.stdin.readline

m = int(input())
n = int(input())
m = ceil((m**(1/2)))
n = floor((n**(1/2)))
M = []
if m>n:
    print(-1)
else:
    L = list(range(m,n+1))
    for i in range(len(L)):
        M += [L[i]**2]
    print(sum(M))
    print(min(M))