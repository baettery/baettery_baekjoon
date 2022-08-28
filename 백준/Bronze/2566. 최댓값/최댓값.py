import sys
L = []
max_list  = []
for i in range(9):
    s = list(map(int,sys.stdin.readline().split()))
    max_list.append(max(s))
    L.append(s)

m = max(max_list)
idx = max_list.index(max(max_list))

print(m)
print(idx+1, L[idx].index(m)+1)