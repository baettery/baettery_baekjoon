import sys
input = sys.stdin.readline
E, S, M = map(int, input().split())
e = 1; s = 1; m = 1
ans = 0
while e!=E or s!=S or m!=M:
    ans += 1; m += 1; s += 1; e += 1
    if m>19:
        m = 1
    if s>28:
        s = 1
    if e>15:
        e = 1
print(ans+1)