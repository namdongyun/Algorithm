import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())  # M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수, 상자의 수를 나타내는 H
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]
flag = True
result = 0

dq = deque()

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs():
    while dq:
        z, y, x = dq.popleft()
        for i in range(6):
            nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]

            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:     # 좌표가 정상일 때
                if graph[nz][ny][nx] == 0:      # 해당 좌표 토마토가 익지않았을 때
                    graph[nz][ny][nx] = graph[z][y][x] + 1     # 이전 좌표 토마토의 값 + 1
                    dq.append((nz, ny, nx))     # 큐에 좌표 추가


for z in range(H):     # 탐색해서 익은 토마토들의 좌표를 큐에 넣어줌
    for y in range(N):
        for x in range(M):
            if graph[z][y][x] == 1:
                dq.append((z, y, x))

bfs()

for z in range(H):     # 탐색해서 익은 토마토들을 찾음
    for y in range(N):
        for x in range(M):
            if graph[z][y][x] == 0:
                flag = False
                break
            else:
                result = max(result, graph[z][y][x]-1)

if flag:
    print(result)
else:
    print(-1)