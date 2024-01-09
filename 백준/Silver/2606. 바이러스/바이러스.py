import sys

input = sys.stdin.readline

N = int(input())    # 컴퓨터의 수
M = int(input())    # 연결되어 있는 컴퓨터 쌍의 수
pc = 0

graph = [[False] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = True


def dfs(x):
    global pc
    visited[x] = True

    for i in range(1, N+1):
        if graph[x][i] == True and not visited[i]:
            pc += 1
            dfs(i)


dfs(1)
print(pc)