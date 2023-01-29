import sys
from itertools import permutations
input = sys.stdin.readline
N, M = map(int, input().split())
nList = list(range(1, N+1))
ans = list(permutations(nList, M))
for _ in range(len(ans)):
    print(*ans[_])