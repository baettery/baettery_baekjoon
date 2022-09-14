import sys
input = sys.stdin.readline
n, m = map(int, input().split())
L = list(map(int, input().split()))
L.sort()
S = []
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            s = L[i]+L[j]+L[k]
            if s<=m:
                S += [s]

print(max(S))
    