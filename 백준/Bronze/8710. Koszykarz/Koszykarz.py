import sys
from math import ceil, floor
input = sys.stdin.readline
k, w, m = map(int, input().split())
ans = ceil((w-k)/m)
print(ans)