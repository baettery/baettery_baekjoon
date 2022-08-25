import sys
n, m = map(int, sys.stdin.readline().split())
k = [0]
k += list(map(int,sys.stdin.readline().split()))
for i in range(1, n+1):
    k[i] += k[i-1]
for i in range(m):
    a, b = map(int,sys.stdin.readline().split())
    print(k[b]-k[a-1])