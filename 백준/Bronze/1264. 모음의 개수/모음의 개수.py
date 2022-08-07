import sys
while 1:
    n = sys.stdin.readline().strip()
    if n=='#':
        break
    else:
        n = n.lower()
        n = list(n)
        k = n.count('a')+n.count('e')+n.count('i')+n.count('o')+n.count('u')
    print(k)