import sys
input = sys.stdin.readline
n = int(input())
S = set(map(int, input().split()))
L = sorted(S)
for i in range(len(L)):
    print(L[i], end = ' ')