A = int(input())
B = int(input())
C = int(input())

sumStr = str(A*B*C)
num = [0] * 10

for i in sumStr:
    num[int(i)] += 1

for i in num:
    print(i)