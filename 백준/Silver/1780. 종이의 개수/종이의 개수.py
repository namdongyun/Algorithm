import sys

input = sys.stdin.readline


def check(y, x, n):
    initial = graph[y][x]

    for i in range(y, y+n):
        for j in range(x, x+n):
            if graph[i][j] != initial:
                return False
    return True


def solution(y, x, n):
    global minus, zero, plus

    if check(y, x, n):
        if graph[y][x] == -1:
            minus += 1
        elif graph[y][x] == 0:
            zero += 1
        elif graph[y][x] == 1:
            plus += 1
    else:
        nn = n//3
        for i in range(3):
            for j in range(3):
                solution(y + nn*i, x + nn*j, nn)


N = int(input().rstrip())    # N
graph = [list(map(int, input().split())) for _ in range(N)]     # 종이 그래프

minus, zero, plus = 0, 0, 0

solution(0, 0, N)

print(minus, zero, plus, sep='\n')
