import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    H, W, N = map(int,input().split())
    if N%H !=0:
        last = N//H + 1
    else:
        last = N//H
    if N%H ==0:
        first = H
    else: 
        first = N%H
    print(first*100+last)