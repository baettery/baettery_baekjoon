import sys
a= sys.stdin.readline().strip()
a = list(a)
b = [0]*len(a)
for i in range(len(a)):
    if (a[i]).isupper()==True:
        b[i] = a[i].lower()
    else:
        b[i] = a[i].upper()

c = ''.join(b)
print(c)