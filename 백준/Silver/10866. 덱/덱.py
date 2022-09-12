import sys
input = sys.stdin.readline
n = int(input())
L = []
for i in range(n):
    order = input().strip()
    if order == 'pop_front':
        if len(L)==0:
            print(-1)
        else:
            print(L[0])
            L = L[1:]
    elif order == 'pop_back':
        if len(L)==0:
            print(-1)
        else:
            print(L[-1])
            L = L[:-1]
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
        if order[5] =='b':
            X = int(''.join(order[10:]))
            L += [X]
        else:
            X = int(''.join(order[11:]))
            L.insert(0, X) 
    