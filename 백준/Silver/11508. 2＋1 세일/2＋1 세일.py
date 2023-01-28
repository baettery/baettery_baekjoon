import sys
input = sys.stdin.readline
N = int(input())
dairyList = [int(input()) for _ in range(N)]
dairyList.sort(reverse=True)
ans = 0
for i in range(N):
    if (i+1)%3!=0:
        ans += dairyList[i]
print(ans)