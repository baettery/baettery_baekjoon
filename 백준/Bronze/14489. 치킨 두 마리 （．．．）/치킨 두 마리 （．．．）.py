import sys
input = sys.stdin.readline
A, B = map(int,input().split())
C = int(input())

if (A+B) >= (C*2):
    print(A+B-2*C)
else:
    print(A+B)