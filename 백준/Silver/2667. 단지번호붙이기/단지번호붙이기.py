import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

count = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

sizeList = []

def bfs(y, x):
    if graph[y][x] == 0 or visited[y][x]:
        return False

    dq = deque()
    dq.append((y, x))
    visited[y][x] = True
    count = 1

    while dq:
        y, x = dq.popleft()

        for j in range(4):
            ny = y + dy[j]
            nx = x + dx[j]

            if nx >= N or nx <= -1 or ny >= N or ny <= -1:  # 좌표를 벗어날 경우
                continue
            if graph[ny][nx] == 0 or visited[ny][nx]:   # 그래프 위치가 0 이거나, 방문 했던 곳일 경우
                continue
                
            dq.append((ny, nx))     # 큐에 좌표 추가
            visited[ny][nx] = True  # 방문 완료 표시
            count += 1

    return count


for y in range(N):
    for x in range(N):
        size = bfs(y, x)
        if size > 0:
            sizeList.append(size)

sizeList.sort()
print(len(sizeList))
for i in sizeList:
    print(i)
