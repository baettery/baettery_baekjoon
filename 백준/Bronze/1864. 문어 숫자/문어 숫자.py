import sys
input = sys.stdin.readline
L = '-\(@?>&%/'
L = list(L)
K = [0,1,2,3,4,5,6,7,-1]
while 1:
    new = input().rstrip()
    if new == '#':
        break
    else:
        N = list(new)
        sum_value = 0
        for i in range(len(N)):
            idx = L.index(N[i])
            sum_value += (8**(len(N)-i-1))*K[idx]
        print(sum_value)