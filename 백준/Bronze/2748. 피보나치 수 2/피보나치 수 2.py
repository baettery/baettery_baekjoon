import sys
m = int(sys.stdin.readline())
L = [0,1]
def fib(n):
    if n<len(L):
        return L[n]
    else:
        f = fib(n-1)+fib(n-2)
        L.append(f)
        return f
print(fib(m))