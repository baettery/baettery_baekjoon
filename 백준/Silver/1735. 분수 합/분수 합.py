import sys
from math import lcm, gcd
input = sys.stdin.readline
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
denominator = lcm(a2,b2)
numerator = (denominator//a2)*a1 + (denominator//b2)*b1
if gcd(denominator, numerator)!=1:
    n = gcd(denominator, numerator)
    denominator = denominator//n
    numerator = numerator//n
print(numerator, denominator)