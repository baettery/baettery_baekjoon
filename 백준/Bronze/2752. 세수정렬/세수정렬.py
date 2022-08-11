import sys
a,b,c = map(int,sys.stdin.readline().split())
list1 = [a,b,c]
list1.sort()
for i in range(3):
    print(list1[i],end=' ')