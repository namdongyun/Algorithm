numList = []
for _ in range(7):
    numList.append(int(input()))

oddNumList = []

for i in range(len(numList)):
    if numList[i] % 2 == 1:
        oddNumList.append(numList[i])

if not oddNumList:
    print(-1)
else:
    print(sum(oddNumList))
    print(min(oddNumList))
