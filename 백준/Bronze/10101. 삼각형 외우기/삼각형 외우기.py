import sys
a, b, c = [int(sys.stdin.readline()) for i in range(3)]
if a+b+c != 180:
    print('Error')
elif a==b==c:
    print('Equilateral')
elif (a==b)|(b==c)|(c==a):
    print('Isosceles')
else:
    print('Scalene')