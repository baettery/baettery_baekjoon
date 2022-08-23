import sys 
n = int(sys.stdin.readline())
car_list = list(map(int,sys.stdin.readline().split()))
print(car_list.count(n))