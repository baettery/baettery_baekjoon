import sys
input = sys.stdin.readline
t = int(input()) 

def cal(n):
    if n==1:
        return 0 
    elif n==2:
        return 1
    elif n==3:
        return 1
    cal_list = [0,0,1,1] #index 때문에 앞에 0 삽입

    for i in range(4, n+1):
        if i%3 == 0:
            num1 = 1 + cal_list[i-1]
            num = cal_list[i//3] + 1
            if i%2 ==0:
                num2 = cal_list[i//2] +1
            else:
                num2 = num1
            cal_list.append(min(num1,num,num2))
        elif i%2 == 0:
            num1 = 1 + cal_list[i-1]            
            num = cal_list[i//2] + 1
            cal_list.append(min(num1,num))
        else:      
            num = cal_list[i-1] + 1
            cal_list.append(num)
    return cal_list[-1]
    

print(cal(t))
