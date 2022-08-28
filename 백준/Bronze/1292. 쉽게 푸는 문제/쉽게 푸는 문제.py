import sys
a, b = map(int, input().split())
L = []
for i in range(b+1):
    L += [i]*i
s = 0
for i in range(a-1,b):
    s += L[i]
print(s)