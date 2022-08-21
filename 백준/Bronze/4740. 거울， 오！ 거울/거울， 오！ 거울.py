import sys 
while 1:
    sentence = input()
    if sentence == '***':
        break
    else:
        sentence = list(sentence)
        sentence.reverse()
        print(*sentence,sep='')