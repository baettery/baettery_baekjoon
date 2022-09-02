import sys
input = sys.stdin.readline
X = int(input())
N = int(input())
A = [0]*N
B = [0]*N
for i in range(N):
    A[i], B[i] = map(int,input().split())
k = 0
for i in range(N):
    k += A[i]*B[i]
if k==X:
    print('Yes')
else:
    print('No')