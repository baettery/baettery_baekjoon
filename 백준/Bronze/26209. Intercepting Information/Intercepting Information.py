import sys
input = sys.stdin.readline
L = list(map(int, input().split()))
if 9 in L:
    print('F')
else:
    print('S')