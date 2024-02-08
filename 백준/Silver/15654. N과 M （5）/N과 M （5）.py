import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

numList = list(map(int, input().split()))
numList.sort()

s = []

def solution(dq):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for i in dq:
        s.append(i)
        dq2 = deque(dq)
        dq2.remove(i)
        solution(dq2)
        s.pop()

solution(numList)