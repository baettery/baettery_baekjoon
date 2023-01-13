n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(b):
        print('X'*a)
    print('')