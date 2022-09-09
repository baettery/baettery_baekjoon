import sys
input = sys.stdin.readline
Scale = '12345678'
Scale = list(Scale)
Scale_rev = list(reversed(Scale))

L = list(input().strip().split())
if L == Scale:
    print('ascending')
elif L == Scale_rev:
    print('descending')
else:
    print('mixed')
