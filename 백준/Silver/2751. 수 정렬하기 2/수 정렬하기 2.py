import sys
n = int(sys.stdin.readline())
num_list = [int(sys.stdin.readline().strip()) for i in range(n)]
num_list.sort()
print(*num_list,sep='\n')