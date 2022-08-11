import sys
n = int(sys.stdin.readline())
print('Gnomes:')
for i in range(n):
    a,b,c = map(int,sys.stdin.readline().split())
    list1 = [a,b,c]
    list2 = [a,b,c]
    list3 = [a,b,c]
    list3.sort(reverse=True)
    list2.sort()
    if (list1 ==list2)|(list1==list3):
        print('Ordered')
    else:
        print('Unordered')