import sys
input = sys.stdin.readline
n, m = map(int, input().split())
L = [0]*n
for i in range(n):
    L[i] = list(input().strip())

length = 0
for i in range(n):
    for j in range(m):
        if i%2==0:
            if j+1<m:
                if L[i][j] != L[i][j+1]:
                    length +=1
            if i+1<n:
                if L[i][j] != L[i+1][j]:
                    length +=1
            if i+1<n and j-1>=0:
                if L[i][j] != L[i+1][j-1]:
                    length +=1
        else:
            if j+1<m:
                if L[i][j] != L[i][j+1]:
                    length +=1
            if i+1<n:
                if L[i][j] != L[i+1][j]:
                    length +=1
            if i+1<n and j+1<m:
                if L[i][j] != L[i+1][j+1]:
                    length +=1     
print(length)    