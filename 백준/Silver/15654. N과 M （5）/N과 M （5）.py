import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

numList = list(map(int, input().split()))
numList.sort()

s = []

def solution():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for i in range(N):
        if numList[i] in s:
            continue
        s.append(numList[i])
        solution()
        s.pop()

solution()
