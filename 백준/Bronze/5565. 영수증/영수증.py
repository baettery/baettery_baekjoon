import sys
input = sys.stdin.readline
n = int(input())
sum9 = 0
for i in range(9):
    k = int(input())
    sum9 += k
print(n-sum9)