import sys
input = sys.stdin.readline
n = int(input())
L = [0]
L += list(map(int,input().split()))
num_count = 0
tot = 0
for i in range(1,n+1):
    if L[i] ==0 :
        num_count = 0
    else:
        num_count += 1
        tot += num_count
print(tot)