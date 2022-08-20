import sys
t = int(sys.stdin.readline())
a = 5*60; b = 1*60; c = 10
if t%10 !=0:
    print(-1)
else:
    num1 = t//a
    num2 = (t%a)//b
    num3 = ((t%a)%b)//c
    print(num1, num2, num3)