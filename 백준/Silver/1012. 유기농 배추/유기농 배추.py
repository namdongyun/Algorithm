import sys
from collections import deque

sys.setrecursionlimit(10**6)    # 재귀함수 1000 제한 해제
input = sys.stdin.readline

T = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(y, x):
    if x <= -1 or x >= M or y <= -1 or y >= N:
        return False
    else:
        if graph[y][x] == 1:
            graph[y][x] = 0

            for j in range(4):
                ny = y + dy[j]
                nx = x + dx[j]
                dfs(ny, nx)
            return True
        return False


for _ in range(T):  # 테스트 케이스 만큼 반복
    count = 0   # 필요한 배추흰지렁이 개수
    M, N, K = map(int, input().split())  # 배추밭의 가로길이, 세로길이, 배추가 심어져 있는 위치의 개수

    graph = [[0] * M for _ in range(N)]  # 배추밭 그래프 생성

    for i in range(K):  # 위치의 개수 만큼 반복하여 배추가 심어져 있는 위치의 값을 1로 변경
        x, y = map(int, input().split())
        graph[y][x] = 1

    for x in range(M):
        for y in range(N):
            if dfs(y, x):
                count += 1
    print(count)
