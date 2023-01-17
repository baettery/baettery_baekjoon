import sys
input = sys.stdin.readline
n, k = map(int, input().split())

def pascal(x):
    pasList = [[1], [1,1]]
    for i in range(2, x):
        k = [1]
        for j in range(len(pasList[i-1])-1):
            k.append(pasList[i-1][j]+ pasList[i-1][j+1])
        k.append(1)
        pasList.append(k)
    return pasList

if n == 1 or n == 2:
    print(1)
else:
    l = pascal(n)
    print(l[n-1][k-1])