import sys
input = sys.stdin.readline
apple = [int(input()) for i in range(3)]
banana = [int(input()) for i in range(3)]
apple_score = apple[0]*3 + apple[1]*2 + apple[2]
banana_score = banana[0]*3 + banana[1]*2 + banana[2]
if apple_score > banana_score:
    print('A')
elif apple_score < banana_score:
    print('B')
else:
    print('T')