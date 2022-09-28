import sys
input = sys.stdin.readline
n = int(input())
money = [25, 10, 5, 1]
for i in range(n):
    count = [0,0,0,0]
    m = int(input())

    for j in range(4):

        if m==0:
            break
        elif m//money[j]>0:
            count[j] = m//money[j]
            m = m%money[j]

    print(*count)
