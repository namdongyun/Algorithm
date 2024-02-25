import sys

input = sys.stdin.readline

N, M = map(int, input().split())        # 방의 크기 N x M
r, c, d = map(int, input().split())     # 처음 로봇 청소기가 있는 좌표 (r, c), 처음 로봇 청소기의 방향 d
room = [list(map(int, input().split())) for _ in range(N)]  # 각 칸의 값이 (0 -> 청소x, 1 -> 벽)

result = 0  # 로봇 청소기가 작동을 멈출 때까지 청소하는 칸의 개수

dy = [-1, 0, 1, 0]      # 북, 동, 남, 서
dx = [0, 1, 0, -1]


def solution(y, x, d):
    global result
    flag = 0

    if room[y][x] == 0:     # 현재 칸이 청소되지 않은 경우 청소하기
        room[y][x] = 2
        result += 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if room[ny][nx] == 0:
            flag = 1    # 주변에 청소가 안된 칸이 있는 경우 1
            break

    if flag == 1:       # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
        for j in range(1, 5):
            nd = d - j  # 반시계 방향으로 90도 회전
            if nd < 0:
                nd = 4 + nd

            ny = y + dy[nd]
            nx = x + dx[nd]

            if room[ny][nx] == 0:   # 칸이 청소되지 않은 경우
                solution(ny, nx, nd)
                break

    elif flag == 0:     # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
        nd = d - 2  # 반대 방향 후진
        if nd < 0:
            nd = 4 + nd

        ny = y + dy[nd]
        nx = x + dx[nd]

        if room[ny][nx] == 1:   # 뒤쪽 칸이 벽이라면
            return

        solution(ny, nx, d)


solution(r, c, d)
print(result)
