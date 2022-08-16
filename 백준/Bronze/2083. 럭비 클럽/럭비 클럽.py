import sys
while 1:
    a, b, c = sys.stdin.readline().split()
    b = int(b)
    c = int(c)
    if (a=='#')&(b==0)&(c==0):
        break
    else:
        if (b>17)|(c>=80):
            print(a,'Senior')
        else:
            print(a,'Junior')