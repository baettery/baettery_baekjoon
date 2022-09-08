import sys
input = sys.stdin.readline
a, b = map(int,input().split())
L_A = set(map(int,input().split()))
L_B = set(map(int,input().split()))
print(len(L_A.union(L_B)) - len(L_A.intersection(L_B)))