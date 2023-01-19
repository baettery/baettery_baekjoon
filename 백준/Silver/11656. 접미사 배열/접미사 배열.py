import sys
input = sys.stdin.readline
N = input().strip()
ans = []
for i in range(len(N)):
    ans.append(N[i:])
ans.sort()
print(*ans, sep = '\n')