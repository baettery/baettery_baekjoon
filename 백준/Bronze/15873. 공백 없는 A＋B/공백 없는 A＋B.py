import sys
n = int(sys.stdin.readline())
k = list(str(n))
if len(k) == 2:
    print(n%10 + n//10)
elif len(k) == 4:
    print(20)
else:
    k = list(map(int,k))
    if k[-1] == 0:
        print(k[0]+10)
    else:
        print(10+k[-1])

