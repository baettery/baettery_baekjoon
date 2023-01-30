import sys
input = sys.stdin.readline
N = int(input())

def fib(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        L = [0, 1]
        for _ in range(1,N):
            L.append(L[-1]+L[-2])
        return L[-1]

print(fib(N))