import sys
t = int(sys.stdin.readline())
for i in range(t):
    n = sys.stdin.readline().strip()
    n = list(str(n))
    print(*n[0],*n[-1],sep='')