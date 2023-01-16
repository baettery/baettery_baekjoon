import sys
input = sys.stdin.readline
s = list(input().strip())
l = len(s)

thr = 0
nextList = []
if 'U' in s:
    uIdx = s.index('U')
    if uIdx != l-1:
        nextList = s[uIdx+1:]
        thr = 1
if thr == 1 and 'C' in nextList:
    cIdx = nextList.index('C')
    if cIdx != l-1:
        nextList = nextList[cIdx+1:]
        thr = 2
if thr == 2 and 'P' in nextList:
    pIdx = nextList.index('P')
    if pIdx != l-1:
        nextList = nextList[pIdx+1:]
        thr = 3
if thr == 3 and 'C' in nextList:
    thr = 4
if thr == 4:
    print('I love UCPC')
else:
    print('I hate UCPC')