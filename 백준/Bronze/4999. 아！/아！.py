import sys
n = sys.stdin.readline().strip()
m = sys.stdin.readline().strip()

n = len(list(n))
m = len(list(m))

if n<m:
    print('no')
else:
    print('go')