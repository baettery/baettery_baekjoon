import sys
input = sys.stdin.readline
while 1:
    m, n, l = map(int, input().split())
    if m==0:
        break
    else:
        L = [m,n,l]
        L.sort()
        if L[0]+L[1]<=L[2]:
            print('Invalid')
        else:
            if m==n==l:
                print('Equilateral')
            elif (m!=n)&(n!=l)&(l!=m):
                print('Scalene')
            else:
                print('Isosceles')