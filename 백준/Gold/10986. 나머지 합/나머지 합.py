import sys

input = sys.stdin.readline

N, M = map(int, input().split())       # N개 수, 합을 나눌 M값
table = list(map(int, input().split()))     # 입력받을 리스트
numIndex = [0] * M      # S 배열 값을 M으로 나눈 나머지 값 인덱스 배열

S = [0] * N
S[0] = table[0]

for i in range(1, N):
    S[i] = S[i-1] + table[i]

result = 0

for i in range(N):
    remain = S[i] % M
    if remain == 0:
        result += 1
    numIndex[remain] += 1

for i in range(M):
    if numIndex[i] > 1:
        result += (numIndex[i] * (numIndex[i]-1)) // 2

print(result)


