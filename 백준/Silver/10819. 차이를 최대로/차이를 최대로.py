import sys

input = sys.stdin.readline

N = int(input())
numList = list(map(int, input().split()))   # 배열 리스트
visited = [False for _ in range(N)]         # 방문 기록
maxNum = -99999


def solution(start, total, depth):
    global maxNum

    if depth == N - 1:      # 식을 N - 1번 돌았을 때 멈추고 최대값 구하기
        maxNum = max(maxNum, total)
        return

    for i in range(N):  # 모든 경우의 수 진행
        if not visited[i]:  # 방문 기록이 없는 경우
            visited[i] = True
            currentTotal = total + abs(numList[start] - numList[i])     # |A[0] - A[1]| + ... 계산

            solution(i, currentTotal, depth + 1)    # 다음 계산 진행
            visited[i] = False  # 방문 기록 되돌리기


for start in range(N):      # 처음 A[0]에 들어갈 N개의 숫자들을 돌아가며 적용
    visited[start] = True
    solution(start, 0, 0)   # A[0]을 정하고 그 다음 진행
    visited[start] = False  # A[0] 방문기록 되돌리기

print(maxNum)