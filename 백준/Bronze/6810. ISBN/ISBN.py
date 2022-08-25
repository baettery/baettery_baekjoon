import sys
isb = '9780921418'
L = list(isb)

L.append(int(sys.stdin.readline()))
L.append(int(sys.stdin.readline()))
L.append(int(sys.stdin.readline()))
L = list(map(int,L))
answer = 0
for i in range(len(L)):
    if i%2==0:
        answer += L[i]*1
    else:
        answer += L[i]*3
        
print('The 1-3-sum is '+str(answer))