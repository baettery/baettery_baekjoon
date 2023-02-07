import sys
input = sys.stdin.readline
N = int(input())
ans = 0
for i in range(N):
    dday = list(str(input().strip()))
    dday = int(''.join(dday[2:]))
    if dday <= 90:
        ans += 1
print(ans)