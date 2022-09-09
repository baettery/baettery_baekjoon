import sys
input = sys.stdin.readline
while 1:
    n = int(input())
    if n==0:
        break
    else:
        m = list(str(n))
        m = reversed(m)
        m = int(''.join(m))
        if n == m:
            print('yes')
        else:
            print('no')