import sys
input = sys.stdin.readline
N = int(input())
array = [list(input().strip()) for _ in range(N)]
wNum, hNum = 0, 0
for i in range(N):
    wLen, hLen = 0, 0 
    for j in range(N):
        if array[i][j] == '.':
            wLen += 1
        else:
            if wLen >= 2:
                wNum += 1
            wLen = 0
        if j == N-1:
            if wLen >= 2:
                wNum += 1
        # h
        if array[j][i] == '.':
            hLen += 1
        else:
            if hLen >= 2:
                hNum += 1
            hLen = 0
        if j == N-1:
            if hLen >= 2:
                hNum += 1
print(wNum, hNum)

