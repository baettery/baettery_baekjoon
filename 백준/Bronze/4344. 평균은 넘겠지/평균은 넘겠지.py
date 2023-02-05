import sys
input = sys.stdin.readline
C = int(input())
for _ in range(C):
    L = list(map(int, input().split()))
    count = L[0]
    mean = sum(L[1:])/count
    ans = 0
    for i in range(1, len(L)):
        if L[i] > mean:
            ans += 1
    print(f'{(ans/count)*100:.3f}%')