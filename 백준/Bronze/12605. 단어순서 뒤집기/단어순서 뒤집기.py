import sys
input = sys.stdin.readline
N = int(input())
for i in range(N):
    L = list(input().strip().split())
    sentence = ' '.join(L[::-1])
    print(f'Case #{i+1}: {sentence}')