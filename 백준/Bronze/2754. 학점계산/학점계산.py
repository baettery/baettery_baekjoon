import sys
L = list(sys.stdin.readline().strip())
score = 0; score1 = 0
abc = list('ABCDEF')
plus = list('+0-')

if len(L) == 1:
    score = 0.0
else:
    idx = abc.index(L[0])
    score = 4-idx

if len(L) == 1:
    score1 = 0.0
else:
    idx2 = plus.index(L[1])

    if idx2 ==0:
        score1 += 0.3
    elif idx2 == 2:
        score1 += -0.3
    else:
        score1 += 0.0
print(score+ score1)
