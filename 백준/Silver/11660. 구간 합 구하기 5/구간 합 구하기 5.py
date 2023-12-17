import sys

input = sys.stdin.readline

N, count = map(int, input().split())  # N x N 표, 합 구하는 횟수

table = [[0] * (N+1)]  # 2차원 (N+1) x (N+1) 배열 생성

for i in range(N):
    table_row = [0] + [int(x) for x in input().split()]  # N x N 표 받아서 생성
    table.append(table_row)

S = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        S[i][j] = S[i-1][j] + S[i][j-1] + table[i][j] - S[i-1][j-1]     # 구간 합 구하기

for _ in range(count):
    x1, y1, x2, y2 = map(int, input().split())  # 좌표값 입력 받기
    result = S[x2][y2] - S[x2][y1-1] - S[x1-1][y2] + S[x1-1][y1-1]
    print(result)
