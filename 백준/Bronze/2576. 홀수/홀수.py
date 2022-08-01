import sys
k = 0
list1 =[]
for i in range(7):
    a = int(sys.stdin.readline())
    if a%2 != 0:
        k=k+a
        list1.append(a)
list1.sort()

if len(list1)!=0:
    print(k)
    print(list1[0])
else:
    print(-1)