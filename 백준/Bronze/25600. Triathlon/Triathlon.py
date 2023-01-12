import sys
input = sys.stdin.readline
n = int(input())
array = []
for _ in range(n):
    a, d, g = map(int, input().split())
    if a == (d+g):
        score = a*(d+g)*2
    else:
        score = a*(d+g)
    array.append(score)
print(max(array))