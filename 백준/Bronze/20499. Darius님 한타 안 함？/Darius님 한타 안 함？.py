import sys
k = sys.stdin.readline().strip()
L = k.split('/')
L = list(map(int,L))
K = L[0]
D = L[1]
A = L[2]
if (K+A<D) | (D==0):
    print('hasu')
else:
    print('gosu')

