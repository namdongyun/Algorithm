import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(y, x):
    dq = deque()
    dq.append((y, x))

    while dq:
        y, x = dq.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if nx<=-1 or nx>=M or ny<=-1 or ny>=N:
                continue
            if graph[ny][nx] == 0:
                continue

            if graph[ny][nx] == 1:
                graph[ny][nx] = graph[y][x] + 1
                dq.append((ny, nx))

    return graph[N-1][M-1]


print(bfs(0, 0))
