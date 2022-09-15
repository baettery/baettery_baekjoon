import sys
input = sys.stdin.readline
while 1:
    m, n = map(int, input().split())
    if m==0 & n==0:
        break
    else:
        print(m+n)