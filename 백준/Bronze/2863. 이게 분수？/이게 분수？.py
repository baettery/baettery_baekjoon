import sys
input = sys.stdin.readline
a, b = map(int, input().split())
c, d = map(int, input().split())
L = [((a/c)+(b/d)), ((c/d)+(a/b)), ((d/b)+(c/a)), ((b/a)+(d/c))]

M = sorted(L)
if M[0]==M[1]:
    print(M[0])
else:
    print(L.index(max(L)))