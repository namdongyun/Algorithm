import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())    # R은 미로 행의 개수, C는 열의 개수

graph = []

visited_f = [[0 for _ in range(C)] for _ in range(R)]   # 불의 방문 기록
visited_j = [[0 for _ in range(C)] for _ in range(R)]   # 지훈의 방문 기록

j_dq = deque()
f_dq = deque()

for i in range(R):
    tmp = list(input().rstrip())

    for j in range(len(tmp)):
        if tmp[j] == 'J':
            j_dq.append((i, j))       # 지훈이의 위치
            visited_j[i][j] = 1  # 지훈이가 있는 좌표의 방문 기록을 1로 초기화
        elif tmp[j] == 'F':
            f_dq.append((i, j))       # 지훈이의 위치
            visited_f[i][j] = 1   # 불이 있는 좌표의 방문 기록을 1로 초기화

    graph.append(tmp)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs():
    while f_dq:     # 불 bfs
        f_y, f_x = f_dq.popleft()

        for i in range(4):
            nf_y, nf_x = f_y + dy[i], f_x + dx[i]   # 불이 상하 좌우로 퍼짐

            if 0 <= nf_y < R and 0 <= nf_x < C:
                if graph[nf_y][nf_x] != '#' and not visited_f[nf_y][nf_x]:    # 벽이 아니고, 방문하지 않은 곳 이여야 함
                    f_dq.append((nf_y, nf_x))             # 불이 퍼진 위치를 큐에 넣음
                    visited_f[nf_y][nf_x] = visited_f[f_y][f_x] + 1     # 불이 붙은 좌표에 이전 좌표 값 + 1분 저장

    while j_dq:     # 지훈 bfs
        j_y, j_x = j_dq.popleft()

        for i in range(4):
            nj_y, nj_x = j_y + dy[i], j_x + dx[i],

            if nj_y >= R or nj_y < 0 or nj_x >= C or nj_x < 0:
                return visited_j[j_y][j_x]  # 배열을 벗어나면 통과이므로 이전 방문 좌표의 값이 걸린 시간임

            if graph[nj_y][nj_x] != '#' and not visited_j[nj_y][nj_x]:  # 벽이 아니고, 방문하지 않은 곳 이여야 함
                if visited_f[nj_y][nj_x] > visited_j[j_y][j_x] + 1 or not visited_f[nj_y][nj_x]:     # 불 방문기록 시간이 지훈 방문기록 시간보다 커야함 (불 보다 지훈이가 먼저 이동해야하니까)
                                                                                                    # 또는 지훈이 방문할 좌표에 불이 방문한 기록이 없어도 됨
                    j_dq.append((nj_y, nj_x))
                    visited_j[nj_y][nj_x] = visited_j[j_y][j_x] + 1     # 지훈이가 움직인 좌표에 이전 좌표 값 + 1분 저장

    return "IMPOSSIBLE"


print(bfs())