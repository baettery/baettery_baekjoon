import sys
input = sys.stdin.readline
idx = 1
while 1:
    l, p, v = map(int, input().split())
    if l == p == v == 0:
        break
    else:
        q = v//p
        r = v%p
        if r>=l:
            count = q*l + l
        else:
            count = q*l + r
        print(f'Case {idx}: {count}')
    idx = idx+1
