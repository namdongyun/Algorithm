oddNumList = []

for i in range(7):
    num = int(input())
    if num % 2 == 1:
        oddNumList.append(num)

if not oddNumList:
    print(-1)
else:
    print(sum(oddNumList))
    print(min(oddNumList))
