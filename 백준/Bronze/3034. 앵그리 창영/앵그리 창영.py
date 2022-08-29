from hashlib import sha512
import sys
input = sys.stdin.readline
N, W, H = map(int,input().split())
for i in range(N):
    n = int(input())
    if (n>(W**2+H**2)**(1/2)):
        print('NE')
    else:
        print('DA')