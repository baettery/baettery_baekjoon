import sys
input = sys.stdin.readline
N = int(input())
student = [] # (Name, Kor, Eng, Math)
for _ in range(N):
    name, kor, eng, math = map(str, input().strip().split())
    kor = int(kor); eng = int(eng); math = int(math)
    student.append((name, kor, eng, math))

student = sorted(student, key = lambda x: (-x[1], x[2], -x[3], x[0]))
for i in range(N):
    print(student[i][0])