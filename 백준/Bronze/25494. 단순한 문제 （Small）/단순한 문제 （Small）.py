import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    count = 0
    a, b, c = map(int, input().split())
    for j in range(1,a+1):
        for k in range(1,b+1):
            for m in range(1, c+1):
                if j%k == k%m == m%j:
                    count+=1
    print(count)
