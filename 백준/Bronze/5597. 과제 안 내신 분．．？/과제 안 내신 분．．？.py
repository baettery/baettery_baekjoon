import sys
input = sys.stdin.readline
L = []
K = list(range(1,31))
for i in range(28):
    L+=[int(input())]

for j in range(30):
    if K[j] not in L:
        print(K[j])