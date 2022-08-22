import sys 
m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
if m<2:
    print('Before')
elif (m==2)&(n<18):
    print('Before')
elif (m==2)&(n==18):
    print('Special')
else:
    print('After')