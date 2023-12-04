listNum = []

for _ in range(5):
    listNum.append(int(input()))

listNum.sort()

print(int(sum(listNum)/5))
print(listNum[2])