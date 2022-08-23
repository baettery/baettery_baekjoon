import sys 
num_list = list(map(int,sys.stdin.readline().split()))
num_1 = num_list.count(1)
num_2 = num_list.count(2)

if num_1>num_2:
    print(1)
else:
    print(2)