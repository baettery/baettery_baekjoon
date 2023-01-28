import sys
from itertools import permutations
input = sys.stdin.readline
N = int(input()) 
K = int(input())
cardList = [input().strip() for _ in range(N)]
nList = list(permutations(cardList, K))
ans = []
for i in range(len(nList)):
    ans.append(int(''.join(nList[i])))
ans = set(ans)
print(len(ans))

