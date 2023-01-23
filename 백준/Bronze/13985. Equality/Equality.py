import sys
input = sys.stdin.readline
ans = list(input().strip())
if int(ans[0]) + int(ans[4]) == int(ans[-1]):
    print('YES')
else:
    print('NO')
