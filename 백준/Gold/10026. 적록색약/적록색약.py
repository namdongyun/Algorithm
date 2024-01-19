import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = [list(input().rstrip()) for _ in range(N)]  # 입력 받은 그래프

visited1 = [[False for _ in range(N)] for _ in range(N)]  # 방문 기록 초기화
visited2 = [[False for _ in range(N)] for _ in range(N)]  # 방문 기록 초기화

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

count1 = 0
count2 = 0

def bfs1(y, x):
    dq1 = deque()

    dq1.append((y, x))

    size1 = 1

    while dq1:
        y, x = dq1.popleft()
        visited1[y][x] = True

        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]

            if 0 <= ny < N and 0 <= nx < N and not visited1[ny][nx]:
                if graph[ny][nx] == graph[y][x]:
                    visited1[ny][nx] = True
                    size1 += 1
                    dq1.append((ny, nx))

    return size1

def bfs2(y, x):
    dq2 = deque()

    dq2.append((y, x))

    size2 = 1

    while dq2:
        y, x = dq2.popleft()
        visited2[y][x] = True

        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]

            if 0 <= ny < N and 0 <= nx < N and not visited2[ny][nx]:
                if graph[ny][nx] == graph[y][x]:
                    visited2[ny][nx] = True
                    size2 += 1
                    dq2.append((ny, nx))
                elif graph[ny][nx] == 'R' or graph[ny][nx] == 'G':
                    if graph[y][x] == 'R' or graph[y][x] == 'G':
                        visited2[ny][nx] = True
                        size2 += 1
                        dq2.append((ny, nx))

    return size2

for i in range(N):
    for j in range(N):
        if not visited1[i][j]:
            s1 = bfs1(i, j)
            if s1 > 0:
                count1 += 1
        if not visited2[i][j]:
            s2 = bfs2(i, j)
            if s2 > 0:
                count2 += 1

print(count1, count2)
