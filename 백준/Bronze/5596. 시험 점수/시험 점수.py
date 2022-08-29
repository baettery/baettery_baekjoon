import sys
input = sys.stdin.readline
L1 = list(map(int,input().split()))
L2 = list(map(int,input().split()))
s1 = sum(L1)
s2 = sum(L2)
if s1>=s2:
    print(s1)
else:
    print(s2)