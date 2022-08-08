import sys
from math import gcd, lcm
a,b = map(int,sys.stdin.readline().split())
print(gcd(a,b))
print(lcm(a,b))