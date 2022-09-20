import sys
from itertools import combinations
input = sys.stdin.readline
count = 0
while 1:
    if count ==0:

        k = list(map(int,input().split()))
        if len(k)==1:
            break
        else:
            L = list(combinations(k[1:], 6))
            for i in range(len(L)):
                print(*list(L[i]))
        count+=1
    else:
        k = list(map(int,input().split()))
        if len(k)==1:
            break
        else:
            print('')
            L = list(combinations(k[1:], 6))
            for i in range(len(L)):
                print(*list(L[i]))