import sys
n, m = map(int,sys.stdin.readline().split())
k = []
for i in range(n):
    a = int(sys.stdin.readline())
    k.append(a)
least = 0

for j in range(n-1,-1,-1):
    if k[j]<= m:
        least = j
        break

q = 0
for s in range(least,-1,-1):
    if m%k[s] == 0:
        q = q + m//k[s]
        break
    else:
        q = q + m//k[s]
        m = m%k[s]
print(int(q))
