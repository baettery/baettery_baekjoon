import sys
input = sys.stdin.readline
n = int(input())

for i in range(n):
    h = 0
    score = 0
    K = list(input().strip())
    for j in range(0,len(K)):
        if K[j] == 'O':
            h += 1
            score += h
        else:
            h = 0
            score = score
    print(score)