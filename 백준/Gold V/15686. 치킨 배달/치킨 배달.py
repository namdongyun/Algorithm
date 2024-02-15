import sys

input = sys.stdin.readline

N, M = map(int, input().split())    # N : NxN인 도시,  M : 폐업시키지 않을 치킨집 최대 갯수
graph = [list(map(int, input().split())) for _ in range(N)]
S = []
home_position = []

result = 99999  # 도시의 치킨 거리 최솟값
length_min = 99999
length_sum = 0


def home_count():
    global home_position

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                home_position.append((i, j))


def solution(start, m_count):
    global result   # 도시의 치킨 거리 최솟값
    global length_min
    global length_sum

    if m_count == M:  # 최대 M개수 도달 시

        for y1, x1 in home_position:
            for y2, x2 in S:
                y_length = abs(y2 - y1)
                x_length = abs(x2 - x1)

                length_min = min(length_min, x_length + y_length)

            length_sum += length_min
            length_min = 99999

        result = min(result, length_sum)
        length_sum = 0
        return

    for i in range(start, N*N):
        y = i // N
        x = i % N

        if graph[y][x] == 2:
            S.append((y, x))    # 치킨 집 좌표 저장
            solution(i + 1, m_count + 1)
            S.pop()


home_count()
solution(0, 0)

print(result)
