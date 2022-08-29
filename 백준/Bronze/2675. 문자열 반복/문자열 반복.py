import sys
input = sys.stdin.readline
n = int(input())

for i in range(n):
    L = []
    r, s = input().strip().split()
    r = int(r)
    s = list(s)
    for j in range(len(s)):
        L += s[j]*r
    print(*L, sep='')
        