import sys
input = sys.stdin.readline
L = list(input().strip())
ABC_list = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
k = 0

for i in range(len(L)):
    idx = ABC_list.index(L[i])
    if idx<=14:
        k +=(ABC_list.index(L[i]))//3 +3
    elif 15<=idx<19:
        k += 8
    elif 19<=idx<22:
        k += 9
    else:
        k += 10   
print(k)