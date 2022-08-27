import sys
input = sys.stdin.readline
abc_l = 'abcdefghijklmnopqrstuvwxyz'
abc_u = abc_l.upper()
abc_list = list(abc_l+abc_u)
num_list = list(range(1,len(abc_list)+1))
k = list(input().rstrip())
s = 0 
for i in range(len(k)):
    idx = abc_list.index(k[i])
    s += num_list[idx]
    
b=0
for j in range(2,s):
    if s%j ==0:
        b=1
if (b==0)|(s==1):
    print('It is a prime word.')
else:
    print('It is not a prime word.')
