import sys 
n = int(sys.stdin.readline())
for i in range(n):
    sentence = sys.stdin.readline().rstrip()
    sentence = list(sentence)
    sentence[0] = sentence[0].upper()
    print(*sentence,sep='')