import sys

input = sys.stdin.readline

def check(y, x, n):
    num = graph[y][x]

    for i in range(y, y+n):
        for j in range(x, x+n):
            if graph[i][j] != num:
                return False
    return True


def solution(y, x, n):
    nn = n//2

    if check(y, x, n):
        if graph[y][x] == 0:
            print(0, end='')
        elif graph[y][x] == 1:
            print(1, end='')
    else:
        print('(', end='')
        for i in range(2):
            for j in range(2):
                solution(y + nn*i, x + nn*j, nn)
        print(')', end='')


N = int(input().rstrip())
graph = [list(map(int, input().rstrip())) for _ in range(N)]

solution(0, 0, N)
