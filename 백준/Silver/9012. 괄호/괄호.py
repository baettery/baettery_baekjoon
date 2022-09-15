import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    L = list(input().strip())
    K = []
    q = 0
    for j in range(len(L)):
        if L[j] == '(':
            K += [1]

        else:
            if len(K) == 0:
                q = 100
                break
            K.pop(-1)

    if (len(K)==0)&(q!=100):
        print('YES')
    else:
        print('NO')