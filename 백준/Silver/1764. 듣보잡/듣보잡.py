import sys
input = sys.stdin.readline
N, M = map(int, input().split())
hear = set(input().strip() for _ in range(N))
see = set(input().strip() for _ in range(M))
ans = hear&see
ans = sorted(list(ans))
print(len(ans))
print(*ans, sep = '\n')