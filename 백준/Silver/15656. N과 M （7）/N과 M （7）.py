import sys

input = sys.stdin.readline

N, M = map(int, input().split())
numList = list(map(int, input().split()))
numList.sort()

s = []

def solution():
    if len(s) >= M:
        print(' '.join(map(str, s)))
        return
    for i in numList:
        s.append(i)
        solution()
        s.pop()

solution()
