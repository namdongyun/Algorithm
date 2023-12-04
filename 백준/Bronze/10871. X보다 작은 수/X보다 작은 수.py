N, X = map(int, input().split())

numArray = list(map(int, input().split()))

for i in range(len(numArray)):
    if numArray[i] < X:
        print(numArray[i], end=" ")