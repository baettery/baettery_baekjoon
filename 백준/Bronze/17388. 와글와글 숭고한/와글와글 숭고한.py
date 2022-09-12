import sys
L = list(map(int, sys.stdin.readline().split()))
K = ['Soongsil', 'Korea','Hanyang']
if sum(L) >= 100:
    print('OK')
else:
    idx = L.index(min(L))
    print(K[idx])