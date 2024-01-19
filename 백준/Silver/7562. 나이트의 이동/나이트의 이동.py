import sys
from collections import deque

input = sys.stdin.readline

testCase = int(input())

dy = [1, 1, 2, 2, -1, -1, -2, -2]
dx = [2, -2, 1, -1, 2, -2, 1, -1]


def bfs():
    while dq:
        y, x = dq.popleft()     # 나이트의 현재 위치 추출

        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < l and 0 <= nx < l and not graph[ny][nx]:
                graph[ny][nx] = graph[y][x] + 1     # 나이트가 이동하는 지점마다 이전 좌표의 값 + 1
                dq.append((ny, nx))

                if ny == dPoY and nx == dPoX:
                    return graph[ny][nx]
        

for _ in range(testCase):
    l = int(input())    # 한 변의 길이
    cPoY, cPoX = map(int, input().split())  # 나이트가 현재 있는 칸
    dPoY, dPoX = map(int, input().split())  # 나이트가 이동하려고 하는 칸

    if cPoY == dPoY and cPoX == dPoX:      # 나이트의 현재 위치 == 이동하려는 위치면 0 출력 후 continue
        print(0)
        continue

    dq = deque()
    dq.append((cPoY, cPoX))     # 나이트의 현재 위치 넣어줌

    graph = [[0 for _ in range(l)] for _ in range(l)]
    graph[cPoY][cPoX] = 1   # 나이트의 현재 위치 좌표에 1값을 넣음

    print(bfs() - 1)
