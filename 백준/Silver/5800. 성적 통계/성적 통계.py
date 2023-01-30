import sys
input = sys.stdin.readline
K = int(input())
classList = [list(map(int, input().split())) for _ in range(K)]
for i in range(K):
    print(f'Class {i+1}')
    sList = sorted(classList[i][1:])
    thr = sList[1]-sList[0]
    for j in range(1, classList[i][0]):
        if sList[j]-sList[j-1] > thr:
            thr = sList[j]-sList[j-1]
    print(f'Max {sList[-1]}, Min {sList[0]}, Largest gap {thr}')