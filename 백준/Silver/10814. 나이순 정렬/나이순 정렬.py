import sys
input = sys.stdin.readline
n = int(input())
age = [0]*n; name = [0]*n
for i in range(n):
    age[i], name[i] = input().strip().split()
age = list(map(int,age))
age_sorted = sorted(age)
before_index = list(range(n))
after_index = sorted(range(n), key = lambda k: age[k])

for j in range(n):
    print(age_sorted[j],name[after_index[j]])