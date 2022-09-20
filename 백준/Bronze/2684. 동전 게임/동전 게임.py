import sys
n = int(input())
Shape = ['TTT','TTH','THT','THH','HTT','HTH','HHT','HHH']
for i in range(n):
    Answer = [0]*8
    seq = list(input().strip())
    for i in range(38):
        idx = Shape.index(seq[i]+seq[i+1]+seq[i+2])
        Answer[idx] +=1
    print(*Answer)