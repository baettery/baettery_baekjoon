import sys
n = int(sys.stdin.readline())
numList = list(range(1,n+1))
ans = []
while len(numList) != 1:
    ans.append(numList.pop(0))
    numList.append(numList.pop(0))

ans.append(numList[0])
print(*ans)