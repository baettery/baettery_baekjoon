import sys
from math import pi, sqrt
input = sys.stdin.readline
a = int(input())
r = sqrt(a/pi)
print(f'{2*pi*r}')