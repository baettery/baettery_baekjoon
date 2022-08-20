import sys
num_list = []
new = 0
for i in range(10):
    off, on = map(int, sys.stdin.readline().split())
    new = new + on - off
    num_list.append(new)
print(max(num_list))
