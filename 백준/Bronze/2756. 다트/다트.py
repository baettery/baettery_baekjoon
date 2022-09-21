import sys
input = sys.stdin.readline
n = int(input())
score = [100,80,60,40,20,0]
def Score(List_player): 
    idx = 0
    answer = 0   
    for i in range(0,3):
        d = ((List_player[idx])**2+(List_player[idx+1])**2)**(1/2)
        if d<=3:
            answer += score[0]
        elif d<=6:
            answer += score[1]
        elif d<=9:
            answer += score[2]
        elif d<=12:
            answer += score[3]
        elif d<= 15:
            answer += score[4]
        else:
            answer += score[5]
        idx += 2
    return answer

for i in range(n):
    L = list(map(float, input().split()))
    # player 1
    player1 = Score(L[0:6])
    player2 = Score(L[6:])
    if player1 == player2:
        print(f'SCORE: {player1} to {player2}, TIE.')
    elif player1 > player2:
        print(f'SCORE: {player1} to {player2}, PLAYER 1 WINS.')
    else:
        print(f'SCORE: {player1} to {player2}, PLAYER 2 WINS.')
