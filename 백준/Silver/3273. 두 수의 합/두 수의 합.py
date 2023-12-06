n = int(input())  # 수열의 크기 n
numList = list(map(int, input().split()))  # 수열에 포함되는 수
numList.sort()
numSum = int(input())  # ai + aj = x

startPo = 0
endPo = n-1
count = 0

while startPo < endPo:
    if numList[startPo] + numList[endPo] == numSum:     # numSum 값과 같다면
        count += 1
        startPo += 1    # 시작 포인터를 1 올림
    elif numList[startPo] + numList[endPo] < numSum:    # numSum 값보다 작다면
        startPo += 1
    else:                                               # numSum 값보다 크다면
        endPo -= 1

print(count)