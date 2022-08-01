a = list(range(1,10000))
list1 = []
for i in range(10000):
    if len(str(i))==1:
        list1.append(i+i)
    if len(str(i))==2:
        list1.append(i+(i//10)+(i%10))
    if len(str(i))==3:
        list1.append(i+(i//100)+((i//10)%10)+(i%10))
    else:
        list1.append(i+(i//1000)+((i//100)%10)+((i//10)%10)+(i%10))
list1 = set(list1)
list1 = list(list1)
sublist = [x for x in a if x not in list1]
for i in range(0,len(sublist)):
    print(sublist[i])