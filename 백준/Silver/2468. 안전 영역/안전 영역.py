import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = []
maxHeight = 0

for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if graph[i][j] > maxHeight:  # 지역 최대 높이 구하기
            maxHeight = graph[i][j]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

result = 0

def bfs(height, y, x):
    dq = deque()
    dq.append((y, x))

    while dq:
        y, x = dq.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue
            if graph[ny][nx] <= height or visited[ny][nx]:
                continue

            visited[ny][nx] = True
            dq.append((ny, nx))


for i in range(maxHeight):
    visited = [[False] * N for _ in range(N)]  # 방문 초기화
    count = 0   # count 초기화

    for j in range(N):
        for k in range(N):
            if graph[j][k] > i and not visited[j][k]:
                bfs(i, j, k)
                count += 1

    result = max(result, count)

print(result)
