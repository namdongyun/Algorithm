import sys
from collections import deque

input = sys.stdin.readline

wheel = [list(input().rstrip()) for _ in range(4)]
dq_wheel = [deque(row) for row in wheel]
K = int(input())
rotation = [list(map(int, input().split())) for _ in range(K)]

result = 0


def solution(wNum, direction):
    if wNum == 0:   # 왼쪽에는 톱니바퀴가 없음
        if dq_wheel[wNum][2] != dq_wheel[wNum + 1][6]:    # 현재 톱니바퀴와 오른쪽 톱니바퀴가 맞닿는 부분의 극이 다를경우
            right(wNum + 1, -direction)
    elif wNum == 3:   # 오른쪽에는 톱니바퀴가 없음
        if dq_wheel[wNum][6] != dq_wheel[wNum - 1][2]:    # 현재 톱니바퀴와 왼쪽 톱니바퀴가 맞닿는 부분의 극이 다를경우
            left(wNum - 1, -direction)
    else:
        if dq_wheel[wNum][2] != dq_wheel[wNum + 1][6]:    # 현재 톱니바퀴와 오른쪽 톱니바퀴가 맞닿는 부분의 극이 다를경우
            right(wNum + 1, -direction)
        if dq_wheel[wNum][6] != dq_wheel[wNum - 1][2]:    # 현재 톱니바퀴와 왼쪽 톱니바퀴가 맞닿는 부분의 극이 다를경우
            left(wNum - 1, -direction)
    
    # 현재 톱니바퀴 돌리기
    if direction == 1:  # 시계방향 돌리기
        dq_wheel[wNum].appendleft(dq_wheel[wNum].pop())
    elif direction == -1:    # 반시계방향 돌리기
        dq_wheel[wNum].append(dq_wheel[wNum].popleft())


def right(wNum, direction):
    if wNum <= 2:
        if dq_wheel[wNum][2] != dq_wheel[wNum + 1][6]:  # 현재 톱니바퀴와 오른쪽 톱니바퀴가 맞닿는 부분의 극이 다를경우
            right(wNum + 1, -direction)

    # 현재 톱니바퀴 돌리기
    if direction == 1:  # 시계방향 돌리기
        dq_wheel[wNum].appendleft(dq_wheel[wNum].pop())
    elif direction == -1:  # 반시계방향 돌리기
        dq_wheel[wNum].append(dq_wheel[wNum].popleft())


def left(wNum, direction):
    if wNum >= 1:
        if dq_wheel[wNum][6] != dq_wheel[wNum - 1][2]:  # 현재 톱니바퀴와 오른쪽 톱니바퀴가 맞닿는 부분의 극이 다를경우
            left(wNum - 1, -direction)

    # 현재 톱니바퀴 돌리기
    if direction == 1:  # 시계방향 돌리기
        dq_wheel[wNum].appendleft(dq_wheel[wNum].pop())
    elif direction == -1:  # 반시계방향 돌리기
        dq_wheel[wNum].append(dq_wheel[wNum].popleft())


for wNum, direction in rotation:
    solution(wNum-1, direction)

for i in range(4):
    if dq_wheel[i][0] == '1':     # 12시방향이 S극인 경우
        result += 2**i

print(result)
