import sys
input = sys.stdin.readline
N = int(input())
if N == 0:
    print("divide by zero")
else:
    L = list(map(int, input().split()))
    ans = sum(L)/N/(sum(L)/N)
    print("%.2f" % ans)