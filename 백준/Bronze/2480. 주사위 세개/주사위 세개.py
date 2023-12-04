diceNum = list(map(int, input().split()))

money = 0

if diceNum[0] == diceNum[1] == diceNum[2]:
    money = 10000 + diceNum[0]*1000
elif diceNum[0] == diceNum[1]:
    money = 1000 + diceNum[0]*100
elif diceNum[1] == diceNum[2]:
    money = 1000 + diceNum[1]*100
elif diceNum[0] == diceNum[2]:
    money = 1000 + diceNum[0]*100
else:
    money = max(diceNum)*100

print(money)