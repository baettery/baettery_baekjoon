import sys
input = sys.stdin.readline
a, b = map(int, input().split())
c = a//2
if b>=c:
    print(c)
else:
    print(b)