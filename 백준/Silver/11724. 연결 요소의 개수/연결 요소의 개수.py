import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())    # 정점의 개수 N과 간선의 개수 M

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

count = 0


def dfs(x):
    visited[x] = True   # 방문 표시
    for i in graph[x]:  # graph[x]와 연결된 정점 모두를 탐색
        if not visited[i]:
            dfs(i)


for j in range(1, N+1):
    if not visited[j]:  # 방문 하지 않았을 경우
        if not graph[j]:  # graph[j] 와 연결된 정점이 없는 경우도 count 올림
            visited[j] = True
            count += 1
        else:
            dfs(j)
            count += 1

print(count)
