import copy
import sys

input = sys.stdin.readline


def solution():
    
    N = int(input())    # 탑의 수
    topList = list(map(int, input().split()))     # 탑의 높이 리스트
    result = [0] * N    # 결과 리스트

    stack = []

    for i in range(N):
        while stack and topList[stack[-1]] < topList[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1] + 1
        stack.append(i)

    return ' '.join(map(str, result))


print(solution())
