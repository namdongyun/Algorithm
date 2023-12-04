A, B = map(int, input().split())

numMin = min(A, B)
numMax = max(A, B)

n = numMax - numMin - 1

if numMax - numMin <= 1:
    n = 0

print(n)

for i in range(numMin+1, numMax):
    print(i, end=" ")
