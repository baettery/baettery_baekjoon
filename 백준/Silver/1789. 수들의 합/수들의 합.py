import sys
from math import sqrt
s = int(sys.stdin.readline())
k = int(sqrt(2*(s+1)))
a = 0
for i in range(k-2,k+3):
    if s < (i*(i+1))/2:
        a = i-1
        break
print(a)