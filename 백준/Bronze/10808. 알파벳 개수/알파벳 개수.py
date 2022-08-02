import sys
n = sys.stdin.readline().strip()
a = list(n)
b = 'abcdefghijklmnopqrstuvwxyz'
b= list(b)
c = [0]*len(b)
for i in range(len(a)):
    k = b.index(a[i])
    c[k] = c[k] +1
for j in range(len(c)):
    print(c[j],end=' ')