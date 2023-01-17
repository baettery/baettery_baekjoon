import sys
input = sys.stdin.readline
H, W = map(int, input().split())
array = []
for _ in range(H):
    k = input().strip()
    array.append(list(k))

thr = -1
for i in range(H):
    thr = -1
    for j in range(W):
        if array[i][j] != 'c' and thr == -1:
            array[i][j] = -1
        elif array[i][j] == 'c':
            thr = 0
            array[i][j] = 0
        else:
            thr += 1
            array[i][j] = thr

for idx in range(H):
    print(*array[idx])
