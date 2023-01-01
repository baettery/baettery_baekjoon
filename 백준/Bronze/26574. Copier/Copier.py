import sys
input = sys.stdin.readline
n = int(input())
L = []
for i in range(n):
    L.append(int(input()))
for i in range(n):
    print(L[i], L[i])