import sys
input = sys.stdin.readline
N = int(input())
array = []
for _ in range(N):
    x, y = map(int, input().split())
    array.append([x, y])
array = sorted(array, key = lambda x: (x[1], x[0]))   
for i in range(N):
    print(*array[i])