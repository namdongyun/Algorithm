numList = [i for i in range(0, 21)]

for i in range(10):
    A, B = map(int, input().split())
    B += 1
    numList_ = numList[:A] + numList[A:B][::-1] + numList[B:]
    numList = numList_

for i in range(1, len(numList)):
    print(numList[i], end=" ")