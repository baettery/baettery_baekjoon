import sys
input = sys.stdin.readline
for i in range(3):
    n = int(input())
    S = [0]*n
    for j in range(n):
        S[j] = int(input())
    ss = sum(S)
    if ss==0:
        print('0')
    elif ss>0:
        print('+')
    else:
        print('-')