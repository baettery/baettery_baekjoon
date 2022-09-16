import sys
input = sys.stdin.readline
L = []
for i in range(9):
    L += [int(input())]
for j in range(8):
    for k in range(j+1,9):
        if j == 0:
            if k != 9:
                S = L[1:k]+L[k+1:]
            else:
                S = L[1:9]
        else:
            if k!=9:
                S = L[0:j]+L[j+1:k]+L[k+1:]
            else:
                S = L[0:j]+L[j+1:k]

        if sum(S) ==100:
            break
    if sum(S) ==100:
        break
print(*S,sep='\n')
