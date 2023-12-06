roomNum = input()

list = [0]*10

for i in roomNum:

    if int(i) == 6 or int(i) == 9:
        
        if list[6] > list [9]:
            list[9] += 1
        else:
            list[6] += 1
    else:
        list[int(i)] += 1

print(max(list))