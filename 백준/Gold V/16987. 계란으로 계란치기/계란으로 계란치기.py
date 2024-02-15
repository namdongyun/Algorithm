import sys
from collections import deque

input = sys.stdin.readline

N = int(input())    # 계란의 수
eggGraph = [list(map(int, input().split())) for _ in range(N)]     # 계란의 내구도, 무게 정보

count = 0


def solution(start):
    global count

    if start >= N:  # 마지막 계란 이후 종료
        brokenEgg = 0
        for i in range(N):  # 깨진 계란 수 세기
            if eggGraph[i][0] <= 0:
                brokenEgg += 1
        count = max(count, brokenEgg)   # 기존 count 값과 brokenEgg중 큰 수를 저장
        return

    if eggGraph[start][0] <= 0:     # 들고 있는 계란이 깨져있으면 다음 계란으로
        solution(start + 1)
        return

    isAllBroken = True
    for k in range(N):
        if k == start:
            continue
        if eggGraph[k][0] > 0:
            isAllBroken = False
            break

    if isAllBroken:     # 들고 있는 계란 이외에 모두 깨져있는 경우
        count = max(count, N-1)
        return

    for i in range(N):
        if i == start:
            continue
        if eggGraph[i][0] <= 0:     # 칠 계란이 깨져 있는 경우
            continue

        eggGraph[start][0] -= eggGraph[i][1]    # 들고 있는 계란의 내구도 - 칠 계란의 무게
        eggGraph[i][0] -= eggGraph[start][1]    # 칠 계란의 내구도 - 들고 있는 계란의 무게
        solution(start + 1)

        eggGraph[start][0] += eggGraph[i][1]    # 기존으로 복구 해서 다른 조합 찾기
        eggGraph[i][0] += eggGraph[start][1]


solution(0)

print(count)


