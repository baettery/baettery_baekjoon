import sys
input = sys.stdin.readline
L = []
i = 0
while 1:
    k = float(input())
    if k == float(999):
        break
    else:
        L += [k]
        if len(L) >1:
            print('{:.2f}'.format(L[i]-L[i-1]))
    i += 1