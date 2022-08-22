import sys 
nn = int(sys.stdin.readline())
nn = list(str(nn))
nn.sort(reverse=True)
print(*nn,sep='')