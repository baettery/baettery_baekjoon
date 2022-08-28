import sys
input = sys.stdin.readline
n = int(input())
L = []
for i in range(n):
    k = input().strip()
    L.append(k[0:1])
S = list(set(L))
A = []
for i in range(len(S)):
    if L.count(S[i])>=5:
        A.append(S[i])
if len(A) == 0:
    print('PREDAJA')
else:
    A.sort()
    print(*A,sep='')