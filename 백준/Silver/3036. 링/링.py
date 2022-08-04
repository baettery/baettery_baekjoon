import sys
from math import gcd as gcd
n = int(sys.stdin.readline())
m = list(map(int,sys.stdin.readline().split()))
for i in range(1,len(m)):
    k = gcd(m[0],m[i])
    print(str(m[0]//k)+'/'+str(m[i]//k))