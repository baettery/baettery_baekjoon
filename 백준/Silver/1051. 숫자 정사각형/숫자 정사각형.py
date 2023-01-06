import sys
input = sys.stdin.readline
N, M = map(int, input().split())
min_nm = min(N, M)
array = []
for _ in range(N):
    k = str(input().strip())
    array.append(list(map(int, list(k))))

# 정사각형 찾기
thr = min_nm-1
ans = 0
while thr>=0 and ans == 0:
    for i in range(N-thr):
        for j in range(M-thr):
            if ans!=0:
                break
            if array[i][j] == array[i][j+thr] == array[i+thr][j] == array[i+thr][j+thr]:
                ans = thr+1              
                break
    thr -= 1

print(ans**2)