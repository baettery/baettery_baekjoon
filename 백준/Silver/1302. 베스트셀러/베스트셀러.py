import sys
input = sys.stdin.readline
n = int(input())
L = []
for i in range(n):
    L += [input().strip()]

S = list(set(L))
S_num = [0]*len(S)
for i in range(len(L)):
    idx =  S.index(L[i])
    S_num[idx] += 1

S_num_max = max(S_num)
N = []
for j in range(len(S_num)):
    if S_num[j] == S_num_max:
        N += [S[j]]
N.sort()
print(N[0])