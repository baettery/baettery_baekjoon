import sys
a, b = map(int,sys.stdin.readline().split())
def func1(x,y):
    print((x+y)*(x-y))
func1(a,b)