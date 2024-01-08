import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())    # 도화지의 세로 크기 n, 가로 크기 m

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

result = 0
maxWidth = 0
W = 0


def dfs(x, y):
    global maxWidth

    if x<=-1 or x>=m or y<=-1 or y>=n:
        return False

    if graph[y][x] == 1:
        graph[y][x] = 0
        maxWidth += 1

        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False


for x in range(m):
    for y in range(n):
        if dfs(x, y):
            result += 1
            W = max(W, maxWidth)
            maxWidth = 0

print(result)
print(W)
