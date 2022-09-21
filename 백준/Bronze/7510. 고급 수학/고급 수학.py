import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    L = list(map(int, input().split()))
    L.sort()
    if L[0]**2 + L[1]**2 == L[2]**2:
        print(f'Scenario #{i+1}:')
        print('yes')
    else:
        print(f'Scenario #{i+1}:')
        print('no')
    print()