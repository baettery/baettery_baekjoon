import sys
from itertools import combinations
input = sys.stdin.readline
N, M = map(int, input().split())
nList = list(range(1, N+1))
ans = list(combinations(nList, M))
for _ in range(len(ans)):
    print(*ans[_])