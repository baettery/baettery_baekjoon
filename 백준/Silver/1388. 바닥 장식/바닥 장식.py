import sys
input = sys.stdin.readline
N, M = map(int, input().split())
array = [list(input().strip()) for _ in range(N)]

ans = 1 # for array[0][0]
# line 1
for i in range(1, M):
    if array[0][i] == '|':
        ans += 1
    else:
        if array[0][i] != array[0][i-1]:
            ans += 1

if N == 1:
    print(ans)
else:
    for i in range(1, N):
        thr = array[i][0]
        if thr == '-' or (thr == '|' and array[i-1][0] != thr):
            ans += 1
        for j in range(1, M): 
            if array[i][j] == '|' and array[i-1][j] != '|':
                ans += 1
            elif array[i][j] == '-' and array[i][j] != array[i][j-1]:
                ans += 1
    print(ans)

