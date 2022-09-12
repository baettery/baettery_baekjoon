import sys
input = sys.stdin.readline
n = int(input())
L = list(map(int, input().split()))
L.sort()
m = int(input())
M = list(map(int, input().split()))

def binary_search(L, low, high, x):
    if high >= low:
        mid = (high+low) //2
        if L[mid] == x:
            return mid
        elif L[mid] > x:
            return binary_search(L, low, mid-1, x)
        else:
            return binary_search(L, mid+1, high, x)
    else:
        return -1
# 함수 https://www.geeksforgeeks.org/python-program-for-binary-search/ 참고
for j in range(m):
    res = binary_search(L, 0 , n-1, M[j])
    if res != -1:
        print(1)
    else:
        print(0)