import sys

input = sys.stdin.readline

N, count = map(int, input().split())  # N x N 표, 합 구하는 횟수

table = [[0] * N for _ in range(N)]  # 2차원 배열 생성

for i in range(N):
    table[i] = list(map(int, input().split()))  # N x N 표 받아서 생성

S = [[0] * N for _ in range(N)]

for i in range(N):
    S[i][0] = table[i][0]

for i in range(0, N):
    for j in range(1, N):
        S[i][j] = S[i][j - 1] + table[i][j]  # S 배열 생성

M = [[0] * 4 for _ in range(count)]

for i in range(count):
    M[i] = list(map(lambda x: int(x) - 1, input().split()))  # (M[0][0],M[0][1]) (M[0][2],M[0][3])
                                                            #      (x1, y1)         (x2, y2)


for i in range(count):
    result = 0
    for j in range(M[i][3] - M[i][1] + 1):
        if M[i][0] == 0:
            result += S[M[i][1] + j][M[i][2]]  # S[x2][y1] - S[x1-1][y1]
        else:
            result += S[M[i][1] + j][M[i][2]] - S[M[i][1] + j][M[i][0] - 1]  # S[x2][y1] - S[x1-1][y1]
    print(result)
