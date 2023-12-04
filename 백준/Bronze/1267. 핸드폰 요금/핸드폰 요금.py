callCount = int(input())
callTime = list(map(int, input().split()))
A = 0
B = 0

for i in range(callCount):
    A += (int(callTime[i] / 30) + 1) * 10
    B += (int(callTime[i] / 60) + 1) * 15

if A < B:
    print("Y", A)
elif B < A:
    print("M", B)
else:
    print("Y", "M", A)