import sys
input = sys.stdin.readline
m, n = map(int,input().split())
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
idx = 0
for k in range(len(primes)):
    if primes[k]>=m:
        idx = k
        break
for i in range(idx,len(primes)):
    print(primes[i])
