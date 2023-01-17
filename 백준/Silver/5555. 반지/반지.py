import sys
input = sys.stdin.readline
suggest = input().strip()
N = int(input())
ans = 0
for _ in range(N):
    k = input().strip()
    if suggest in k:
        ans += 1
    else:
        k = list(k)
        for i in range(9):
            k = k[1:]+ [k[0]]
            if suggest in ''.join(k):
                ans += 1
                break
print(ans)
