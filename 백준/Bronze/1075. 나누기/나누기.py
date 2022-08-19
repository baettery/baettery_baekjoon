import sys
import math
n = int(sys.stdin.readline())
f = int(sys.stdin.readline())
num_list = []

for i in range(0,100):
    new = (n//100)*100 + i
    if new % f == 0:
        num_list.append(i)
minimum = min(num_list)
if len(str(minimum))<=1:
    print(str(minimum).zfill(2))
else:
    print(minimum)