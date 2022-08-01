import sys
n = int(sys.stdin.readline())
list =[]
q1 = n//5
r1 = n%5
q2 = n//3
r2 = n%3
for i1 in range(q1,-1,-1):
    for j1 in range(q2,-1,-1):
        if i1*5+j1*3 == n:
            list.append(i1)
            list.append(j1)
if list==[]:
    print(-1)
else:
    print(list[0]+list[1])