import sys
input = sys.stdin.readline
N = int(input())
crypto = list(map(int, input().split()))
plain = list(input().strip())
plainList = []
for i in range(N):
    if plain[i] == ' ':
        plainList.append(0)
    elif plain[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        plainList.append(ord(plain[i])-64)
    else:
        plainList.append(ord(plain[i])-70)

crypto.sort()
plainList.sort()
if crypto == plainList:
    print('y')
else:
    print('n')