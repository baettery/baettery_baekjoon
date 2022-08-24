import sys
while 1:
    n = sys.stdin.readline().strip()
    if n == 'END':
        break
    else:
        n = list(str(n))
        n.reverse()
        print(*n, sep='')