import sys
n, k = map(int, input().split())
L = list(range(1,n+1))
ans = []
idx = 0
for i in range(n):
    q = L[(idx+(k-1))%len(L)]
    ans += [q]
    idx = L.index(q)
    L.remove(q)
ans = list(map(str,ans))
print('<'+', '.join(ans)+'>')