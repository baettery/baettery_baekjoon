import sys
from math import floor
input = sys.stdin.readline
D, H, W = map(int, input().split())
alpha = ((D**2)/(W**2+H**2))**(1/2)
print(floor(alpha*H), floor(alpha*W))