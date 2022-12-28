import sys
input = sys.stdin.readline
n = int(input())
thr = 0
for i in range(1, 100000000):
    if thr==n:
        break
    if '666' in str(i):
        thr += 1
print(i-1)