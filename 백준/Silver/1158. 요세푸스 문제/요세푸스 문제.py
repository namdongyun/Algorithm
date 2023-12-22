import sys

input = sys.stdin.readline

N, K = map(int, input().split())

result = []
arr = [i for i in range(1, N+1)]
index = 0

for i in range(N):
    index += K-1

    if index >= len(arr):
        index %= len(arr)

    result.append(str(arr.pop(index)))

print("<", ', '.join(result), ">", sep="")
