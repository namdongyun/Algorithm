import copy
import sys

input = sys.stdin.readline

N, M = map(int, input().split())    # N : 세로, M : 가로
graph = []
cctv_list = []
minNum = 99999

for i in range(N):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(M):
        if data[j] in [1, 2, 3, 4, 5]:
            cctv_list.append((data[j], i, j))

cctv = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]], ]                                 # 5번 cctv (동, 서, 남, 북)

# 동 서 남 북
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def solution(depth, graph):
    global minNum
    if depth == len(cctv_list):
        count = 0
        for i in range(N):  # graph에 0이 몇개 있는지 세기
            count += graph[i].count(0)
        minNum = min(minNum, count)     # 최소 사각지대 구하기
        return

    graph_copy = copy.deepcopy(graph)

    cctv_num, y, x = cctv_list[depth]

    for j in cctv[cctv_num]:
        fill(y, x, j, graph_copy)
        solution(depth + 1, graph_copy)
        graph_copy = copy.deepcopy(graph)


def fill(y, x, c, graph_copy):
    for i in c:
        # 현재 cctv 좌표 초기화
        ny = y
        nx = x
        while True:
            ny += dy[i]
            nx += dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M:  # 좌표가 범위를 넘어가면 break
                break
            if graph_copy[ny][nx] == 6:     # 벽일 경우 break
                break
            if graph_copy[ny][nx] == 0:
                graph_copy[ny][nx] = -1     # 감시 가능 표시


solution(0, graph)
print(minNum)
