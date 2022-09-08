import sys
input = sys.stdin.readline
b = input().strip()
k = int(b,2)
k = k*17
print(format(k,'b'))