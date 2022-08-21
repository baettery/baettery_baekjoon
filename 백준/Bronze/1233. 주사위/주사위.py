import sys 
s1, s2, s3 = map(int, sys.stdin.readline().split())
num_list = []
for i in range(1,1+s1):
    for j in range(1,1+s2):
        for k in range(1,1+s3):
            num_list.append(i+j+k)
min1 = min(num_list)
max1 = max(num_list)
new_number = list(range(min1,max1+1))

count_list = [0]*len(new_number)
for i in range(min1, max1+1):
    count_list[i-min1] = num_list.count(i)

idx1 = count_list.index(max(count_list))
print(new_number[idx1])