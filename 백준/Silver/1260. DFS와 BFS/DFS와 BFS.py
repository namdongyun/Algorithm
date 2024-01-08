import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split()) # 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점의 번호 V

graph = [[False] * (N+1) for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = True

visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)


def dfs(v):     # 깊이 우선 탐색
    visited_dfs[v] = True   # 방문 처리
    print(v, end=' ')

    for i in range(1, N+1):
        # 방문 기록이 없고, v 접점과 간선이 있을 경우
        if not visited_dfs[i] and graph[v][i] == True:
            dfs(i)


def bfs(v):     # 너비 우선 탐색
    dq = deque([v])     # 덱 생성
    visited_bfs[v] = True   # 방문 처리

    while dq:
        v = dq.popleft()
        print(v, end=' ')

        for i in range(1, N+1):
            # 방문 기록이 없고, v 접점과 간선이 있을 경우
            if not visited_bfs[i] and graph[v][i] == True:
                dq.append(i)
                visited_bfs[i] = True


dfs(V)  # dfs 결과 출력
print()
bfs(V)  # bfs 결과 출력
