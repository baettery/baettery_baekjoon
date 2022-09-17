import sys
input = sys.stdin.readline
L = list(input().strip())
k = 10
for i in range(1,len(L)):
    if L[i] == L[i-1]:
        k += 5
    else:
        k += 10
print(k)