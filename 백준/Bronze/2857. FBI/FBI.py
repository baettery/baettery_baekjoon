import sys
input = sys.stdin.readline
L = []
for i in range(5):
    k = input().strip()
    if 'FBI' in k:
        L.append(i+1)
if len(L) == 0:
    print('HE GOT AWAY!')
else:
    print(*L)