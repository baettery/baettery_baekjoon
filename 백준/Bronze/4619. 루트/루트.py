from re import S
import sys
from math import trunc
while 1:
    b, n = map(int,sys.stdin.readline().split())
    if b==n==0:
        break
    else:
        s = b**(1/n)
        r = int(trunc(s))
        if abs(r**n -b) < abs((r+1)**n - b):
            print(int(r))
        else:
            print(int(r+1))
