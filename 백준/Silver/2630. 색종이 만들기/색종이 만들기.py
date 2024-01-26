import sys

input = sys.stdin.readline

def check(y, x, n):
    num = graph[y][x]   # 그래프 첫 좌표 값
    for i in range(y, y+n):
        for j in range(x, x+n):
            if graph[i][j] != num:  # 좌표을 값이 다를 경우
                return False
    return True


def solution(y, x, n):
    global zero, plus

    nn = n//2
    if check(y, x, n):
        if graph[y][x] == 0:
            zero += 1
        elif graph[y][x] == 1:
            plus += 1
    else:
        for i in range(2):
            for j in range(2):
                solution(y + nn*i, x + nn*j, nn)


N = int(input().rstrip())
graph = [list(map(int, input().split())) for _ in range(N)]

zero, plus = 0, 0

solution(0, 0, N)
print(zero, plus, sep='\n')