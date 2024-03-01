import sys

input = sys.stdin.readline

k = int(input())
inSignList = list(map(str, input().split()))
numList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
s = []

maxNum = -1
minNum = 10**10


def solution(currentNum, depth):
    global maxNum, minNum

    if depth == k:
        number = "".join(str(n) for n in s)    # s 배열의 숫자들을 문자열로 변환하고 결합
        if int(maxNum) < int(number):
            maxNum = number
        if int(minNum) > int(number):
            minNum = number
        return

    for i in range(10):  # 숫자 리스트
        if numList[i] not in s:  # s배열 안에 numList[i]가 없는 경우만 (중복 방지)
            if inSignList[depth] == '>':    # 부등호가 > 일 경우
                if currentNum > numList[i]:
                    s.append(numList[i])
                    solution(numList[i], depth+1)
                    s.pop()
                else:
                    continue
            elif inSignList[depth] == '<':  # 부등호가 > 일 경우
                if currentNum < numList[i]:
                    s.append(numList[i])
                    solution(numList[i], depth+1)
                    s.pop()


for i in range(10):
    s.append(numList[i])
    solution(numList[i], 0)
    s.pop()

print(maxNum)
print(minNum)