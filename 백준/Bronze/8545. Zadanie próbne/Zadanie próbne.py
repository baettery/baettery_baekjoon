import sys
n = sys.stdin.readline().strip()
n = list(n)
n.reverse()
for i in range(len(n)):
    print(n[i],end='')