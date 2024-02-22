import sys

input = sys.stdin.readline

N = int(input())
graph = [0 for _ in range(N)]
count = 0


def check(y):
    for ny in range(y):
        # 같은 열에 퀸이 있을 경우, 대각선에 퀸이 있을 경우
        if graph[y] == graph[ny] or abs(graph[y] - graph[ny]) == abs(y - ny):
            return False
    return True


def solution(y):
    global count

    if y == N:  # 마지막 퀸 까지 놓았을 경우
        count += 1
        return

    for x in range(N):
        graph[y] = x    # (y, x) 좌표에 퀸을 놓는다
        if check(y):    # (y, x)
            solution(y + 1)


solution(0)
print(count)