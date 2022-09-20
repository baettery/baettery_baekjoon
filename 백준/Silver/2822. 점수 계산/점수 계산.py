import sys
L = []
for i in range(8):
    L += [int(input())]
M = sorted(L)
M = M[3:]
print(sum(M))
for i in range(8):
    if L[i] in M:
        print(i+1,end=' ')
