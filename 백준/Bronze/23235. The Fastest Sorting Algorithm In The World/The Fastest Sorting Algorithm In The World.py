import sys
input = sys.stdin.readline
N = 1
while 1:
    a = list(map(int, input().split()))
    if a == [0]:
        break
    else:
        print(f'Case {N}: Sorting... done!')
        N += 1