import sys
input = sys.stdin.readline
N, K = map(int, input().split())
array = []
for i in range(N):
    k = list(map(int, input().split()))
    k.append(i+1) # 맨 마지막에 몇번째 국가인지 추가
    array.append(k)

array = sorted(array, key = lambda x: (-x[0], -x[1], -x[2]))

rank = 1 # 순위는 1부터 시작
if array[0][-1] == K:
    print(1)
else:
    for j in range(1, N): # 맨 앞에 있는 건 무조건 1등
        if array[j][0:3] != array[j-1][0:3]:
            rank = j+1
        if array[j][-1] == K:
            print(rank)
            break