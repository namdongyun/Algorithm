import sys

input = sys.stdin.readline

N, M = map(int, input().split())

table = [0] + [int(x) for x in input().split()]

S = [0] * (N+1)
for i in range(1, N+1):
    S[i] = S[i-1] + table[i]

count = 0

for i in range(0, N):
    for j in range(1, N+1):
        if (S[j] - S[i]) > 0 and (S[j] - S[i]) % 3 == 0:
            count += 1

print(count)
