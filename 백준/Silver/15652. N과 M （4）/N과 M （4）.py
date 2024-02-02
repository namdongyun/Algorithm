import sys

input = sys.stdin.readline

N, M = map(int, input().split())
s = []

def solution(start):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for i in range(start, N+1):
        s.append(i)
        solution(i)
        s.pop()

solution(1)
