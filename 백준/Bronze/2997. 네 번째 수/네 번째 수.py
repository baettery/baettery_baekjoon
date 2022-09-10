import sys
L = list(map(int,sys.stdin.readline().split()))
L.sort()
diff2_1 = L[2]-L[1]
diff1_0 = L[1]-L[0]
if diff1_0 == diff2_1:
    print(L[2]+diff2_1)
elif diff1_0 == 2*diff2_1:
    print(L[0]+diff2_1)
else:
    print(L[1]+diff1_0)