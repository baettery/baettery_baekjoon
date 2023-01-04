import sys
input = sys.stdin.readline
x = str(input().strip())
if len(x) == 1 or len(x) == 2: # 한 자리 수나 두 자리 수는 모두 한수
    print(int(x)) 
elif len(x) == 3:
    ans = 99
    for i in range(100, int(x)+1):
        i = str(i)
        if int(i[2])-int(i[1]) == int(i[1])-int(i[0]):
            ans += 1
    print(ans)
else:
    print(144) # 예제 참고