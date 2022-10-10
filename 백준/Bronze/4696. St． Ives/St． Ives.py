import sys
input = sys.stdin.readline
while 1:
    n = float(input())
    if n==0:
        break
    else:
        i = 1
        result = 0
        for _ in range(5):
            result = result + i
            i = i*n
        print('%.2f'%result)