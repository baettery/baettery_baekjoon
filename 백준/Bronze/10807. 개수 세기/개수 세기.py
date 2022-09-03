import sys
input = sys.stdin.readline
N = int(input())
L = list(map(int,input().split()))
S = int(input())
print(L.count(S))