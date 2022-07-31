import sys
n = int(sys.stdin.readline())
data = list(map(int, input().split()))
m = max(data)
data = [data[i]/m*100 for i in range(len(data))]
print(sum(data)/len(data))