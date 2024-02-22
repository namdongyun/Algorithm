import sys

input = sys.stdin.readline

N = int(input())
numList = list(map(int, input().split()))
visited = [False for _ in range(N)]
maxNum = -1


def solution(index, total, depth):
    global maxNum

    if depth == N - 1:
        maxNum = max(maxNum, total)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            currentTotal = total + abs(numList[index] - numList[i])

            solution(i, currentTotal, depth + 1)
            visited[i] = False


for start in range(N):
    visited[start] = True
    solution(start, 0, 0)
    visited[start] = False

print(maxNum)