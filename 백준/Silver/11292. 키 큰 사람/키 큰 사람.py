import sys
input = sys.stdin.readline
while True:
    N = int(input())
    if N == 0:
        break
    else:
        studentList = []
        for _ in range(N):
            name, height = input().strip().split()
            height = float(height)
            studentList.append((name, height, _))
        studentList = sorted(studentList, key = lambda x: (-x[1], x[2]))
        thr = studentList[0][1]
        ans = []
        for i in range(N):
            if studentList[i][1] == thr:
                ans.append(studentList[i][0])
            else:
                break
        print(*ans)

