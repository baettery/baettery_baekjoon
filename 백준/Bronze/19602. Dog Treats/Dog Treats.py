import sys
input = sys.stdin.readline
S = int(input())
M = int(input())
L = int(input())
ans = 1 * S + 2 * M + 3 * L
if ans >= 10:
    print('happy')
else:
    print('sad')