import sys
input = sys.stdin.readline
L = list(map(int,input().split()))
K = [0]*6
K[0] = 1 - L[0]
K[1] = 1 - L[1]
K[2] = 2 - L[2]
K[3] = 2 - L[3]
K[4] = 2 - L[4]
K[5] = 8 - L[5]
print(*K)