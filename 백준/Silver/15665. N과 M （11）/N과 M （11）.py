import sys

input = sys.stdin.readline

N, M = map(int, input().split())
numList = list(map(int, input().split()))
numList.sort()

s = []

def solution():
    prev = 0
    if len(s) >= M:
        print(*s)
        return
    for i in numList:
        if prev != i:
            s.append(i)
            prev = i
            solution()
            s.pop()

solution()