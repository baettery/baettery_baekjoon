import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    L = list(input().strip())
    ans = [L[0]]
    for i in range(1, len(L)):
        if L[i] != L[i-1]:
            ans.append(L[i])
    ans = ''.join(ans)
    print(ans)