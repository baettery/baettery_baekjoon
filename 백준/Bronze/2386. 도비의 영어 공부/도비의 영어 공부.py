import sys
input = sys.stdin.readline
while 1:
    n = input().strip()
    n = n.lower()
    if n == '#':
        break
    else:
        L = list(n)
        lower_char = L[0]
        L = L[2:len(L)+1]
        print(lower_char, str(L.count(lower_char)))