import sys

input = sys.stdin.readline

N, M = map(int, input().split())

table = [0] + list(map(int, input().split()))

S = [0] * (N+1)

for i in range(1, N+1):
    S[i] = S[i-1] + table[i]

for i in range(M):
    x1, x2 = map(int, input().split())
    result = S[x2] - S[x1-1]
    print(result)
