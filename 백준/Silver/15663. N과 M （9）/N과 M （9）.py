import sys

input = sys.stdin.readline

N, M = map(int, input().split())
numList = list(map(int, input().split()))
numList.sort()

visited = [False] * N

s = []  # 인덱스 리스트 조합

def solution():
    prev = 0
    if len(s) >= M:
        print(*s)
        return
    for i in range(len(numList)):
        if not visited[i] and prev != numList[i]:
            s.append(numList[i])
            visited[i] = True
            prev = numList[i]
            solution()
            s.pop()
            visited[i] = False

solution()
