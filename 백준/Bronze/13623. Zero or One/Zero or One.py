import sys
A, B, C = map(int,sys.stdin.readline().split())
if A==B==C:
    print('*')
elif (A==B):
    print('C')
elif (A==C):
    print('B')
else:
    print('A')