import sys
input = sys.stdin.readline
L = []
while 1:
    k = int(input())
    if k == -1:
        break
    else:
        L += [k]
print(sum(L))