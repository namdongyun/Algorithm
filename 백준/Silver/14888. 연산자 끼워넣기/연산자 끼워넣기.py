import sys

input = sys.stdin.readline

N = int(input())    # 수의 개수
numList = list(map(int, input().split()))   # 숫자 리스트
operList = list(map(int, input().split()))  # 연산자 리스트 (+, -, *, //)

minNum = 1000000000     # 최소값
maxNum = -1000000000    # 최대값


def solution(depth, result):
    global minNum
    global maxNum

    if depth == N:
        minNum = min(minNum, result)  # 최소값 구하기
        maxNum = max(maxNum, result)  # 최대값 구하기
        return

    for j in range(4):
        if operList[j] >= 1:

            operList[j] -= 1

            if j == 0:
                current_result = result + numList[depth]
            elif j == 1:
                current_result = result - numList[depth]
            elif j == 2:
                current_result = result * numList[depth]
            elif j == 3:
                if result < 0:  # result 값이 음수이면 양수로 변환
                    result = -result
                    current_result = -(result // numList[depth])    # 나눈 뒤 다시 음수로 변환
                else:
                    current_result = (result // numList[depth])

            solution(depth + 1, current_result)

            current_result = result     # current_result 값 되돌리기
            operList[j] += 1            # 연산자 리스트 되돌리기


solution(1, numList[0])

print(maxNum)
print(minNum)
