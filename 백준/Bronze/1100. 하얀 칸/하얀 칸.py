k =0
chess_list = []
for i in range(8):
    n = input()
    chess_list = list(n)
    if i % 2 ==0:
        for j in range(0,8,2):
            if chess_list[j] == 'F':
                k = k+1
    else:
        for j in range(1,9,2):
            if chess_list[j] == 'F':
                k = k+1
print(k)