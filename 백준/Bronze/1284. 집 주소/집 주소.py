import sys
while 1:
    n = int(sys.stdin.readline())
    if n==0:
        break
    else:
        a = list(str(n))
        num0 = a.count('0')
        num1 = a.count('1')
        numother = len(a) - num0 - num1
        k = (len(a)-1) + 2 + num0*4 + num1*2 + numother*3
        print(k)