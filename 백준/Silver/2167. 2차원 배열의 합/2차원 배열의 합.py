import sys
input = sys.stdin.readline
N, M = map(int, input().split())
array = [] # 1차원 prefix sum array
for _ in range(N):
    k = list(map(int, input().split()))
    k = [sum(k[:i+1]) for i in range(M)]
    array.append(k)
K = int(input())
for r in range(K):
    i, j, x, y = map(int, input().split())
    ans = 0
    for u in range(i-1, x):
        if j-1==0:
            ans += array[u][y-1]
        else:
            ans += array[u][y-1]-array[u][j-2]
    print(ans)