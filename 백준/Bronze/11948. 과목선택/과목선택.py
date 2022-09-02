import sys
L = [0]*6
for i in range(6):
    L[i] = int(sys.stdin.readline())
A = L[0:4]
B = L[4:6]
A.sort(reverse=True)
B.sort(reverse=True)
print(sum(A[0:3])+max(B))
