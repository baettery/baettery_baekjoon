import sys
input = sys.stdin.readline
A, B = map(int,input().split())
C, D = map(int, input().split())
k1 = C + B
k2 = A + D
K = [k1,k2]
print(min(K))