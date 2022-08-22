import sys 
from math import ceil
l = int(sys.stdin.readline())
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = int(sys.stdin.readline())
k1 = ceil(a/c)
k2 = ceil(b/d)
if k1>=k2:
    k = k1
else:
    k = k2
print(l-k)