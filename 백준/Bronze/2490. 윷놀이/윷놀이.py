numArray1 = list(map(int, input().split()))
numArray2 = list(map(int, input().split()))
numArray3 = list(map(int, input().split()))

allArray = []
allArray.append(numArray1)
allArray.append(numArray2)
allArray.append(numArray3)

for i in allArray:
    if i.count(0) == 0:
        print("E")
    elif i.count(0) == 1:
        print("A") 
    elif i.count(0) == 2:
        print("B")
    elif i.count(0) == 3:
        print("C")
    elif i.count(0) == 4:
        print("D")