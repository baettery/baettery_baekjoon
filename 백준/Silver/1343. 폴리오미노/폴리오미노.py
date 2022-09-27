import sys
poly = sys.stdin.readline().strip()
poly = poly.replace('XXXX','AAAA')
poly = poly.replace('XX','BB')
if 'X' in poly:
    print(-1)
else:
    print(poly)
