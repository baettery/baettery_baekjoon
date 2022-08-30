import sys
K = int(sys.stdin.readline())
K = 1000-K
L = [500, 100, 50, 10, 5, 1]
q = 0
for i in range(len(L)):
    if K>=L[i]:
        q += K//L[i]
        K = K%L[i]
print(q)
