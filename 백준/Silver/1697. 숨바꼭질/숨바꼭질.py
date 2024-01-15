import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
MAX = 100001
graph = [0] * MAX


def bfs(N):
    dq = deque()
    dq.append(N)

    while dq:
        x = dq.popleft()

        if x == K:
            return graph[x]

        for nx in (x-1, x+1, x*2):
            if 0 <= nx < MAX and not graph[nx]:
                graph[nx] = graph[x] + 1
                dq.append(nx)


print(bfs(N))



