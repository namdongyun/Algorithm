import sys
from collections import deque

input = sys.stdin.readline

n = int(input())    # 전체 사람의 수 n
a, b = map(int, input().split())    # 촌수를 계산해야 하는 서로 다른 두 사람의 번호 a, b
m = int(input())    # 부모 자식들 간의 관계의 개수 m

graph = [[False] * (n+1) for _ in range(n+1)]

for i in range(m):
    start, end = map(int, input().split())
    graph[start][end] = graph[end][start] = True

visited = [0] * (n+1)


def bfs(a, b):
    dq = deque()
    dq.append(a)

    while dq:
        start = dq.popleft()

        for j in range(1, n+1):
            if visited[j] == 0 and graph[start][j] and j != a:
                visited[j] = visited[start] + 1
                dq.append(j)

        if visited[b] != 0:
            return visited[b]

    return -1


print(bfs(a, b))
