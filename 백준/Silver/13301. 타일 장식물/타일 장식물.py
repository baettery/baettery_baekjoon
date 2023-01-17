import sys
input = sys.stdin.readline
N = int(input())
def fibo(x):
    fiboList = [1, 1]
    for i in range(x-2):
        fiboList.append(fiboList[i]+fiboList[i+1])
    return fiboList

if N == 1:
    print(4)
elif N == 2:
    print(6)
else:
    l = fibo(N)
    print(2*(l[-1]+l[-2]) + 2*(l[-2]+l[-3]))