import sys
sys.setrecursionlimit(10**8)

input = sys.stdin.readline

N, M, y, x, K = map(int, input().split())   # 지도의 세로 크기 N, 가로 크기 M, 주사위를 놓은 곳의 좌표 x, y(y, x로 바꿔서 받았음), 명령의 개수 K
graph = [list(map(int, input().split())) for _ in range(N)]     # 지도
command = list(map(int, input().split()))   # 명령 리스트
dice = [0, 0, 0, 0, 0, 0]   # 주사위

dy = [0, 0, 0, -1, 1]   # 동(1), 서(2), 북(3), 남(4)
dx = [0, 1, -1, 0, 0]


def solution(depth, y, x):
    if depth == K:  # 모든 명령을 다 실행 했다면 종료
        return

    ny = y + dy[command[depth]]
    nx = x + dx[command[depth]]

    if ny < 0 or ny >= N or nx < 0 or nx >= M:  # 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시
        solution(depth + 1, y, x)
        return

    turn(command[depth])    # command[depth] 방향으로 주사위 굴리기

    if graph[ny][nx] == 0:  # 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사
        graph[ny][nx] = dice[1]
    else:                   # 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.
        dice[1] = graph[ny][nx]
        graph[ny][nx] = 0

    print(dice[0])  # 주사위가 이동할 때 마다 상단에 쓰여 있는 값을 출력
    solution(depth + 1, ny, nx)


def turn(direction):
    # 위(0), 아래(1), 앞(2), 뒤(3), 왼(4), 오(5)
    n0, n1, n2, n3, n4, n5 = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]

    if direction == 1:  # 동(1), 서(2), 북(3), 남(4)으로 굴리기
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = n4, n5, n2, n3, n1, n0
    elif direction == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = n5, n4, n2, n3, n0, n1
    elif direction == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = n2, n3, n1, n0, n4, n5
    elif direction == 4:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = n3, n2, n0, n1, n4, n5


solution(0, y, x)
