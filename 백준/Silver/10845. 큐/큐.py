import sys
input = sys.stdin.readline
n = int(input())
L = []
for i in range(n):
    order = input().strip()
    if order == 'pop':
        if len(L)==0:
            print(-1)
        else:
            print(L[0])
            L = L[1:]
    elif order == 'size':
        print(len(L))
    elif order == 'empty':
        if len(L)==0:
            print(1)
        else:
            print(0)
    elif order == 'front':
        if len(L) ==0:
            print(-1)
        else:
            print(L[0])
    elif order == 'back':
        if len(L) ==0:
            print(-1)
        else:
            print(L[-1])
    else:
        order = list(order)
        X = int(''.join(order[5:]))
        L += [X]
    