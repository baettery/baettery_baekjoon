import sys
input = sys.stdin.readline
n = int(input())
a, b = map(int, input().split())
c = a//2+b
if n>=c:
    print(c)
else:
    print(n)