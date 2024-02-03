import sys

input = sys.stdin.readline

N, S = map(int, input().split())
numList = list(map(int, input().split()))

s = []

count = 0

def solution(start):
    global count
    if len(s) >= N:
        return
    for i in range(start, N):
        s.append(numList[i])
        if sum(s) == S:
            count += 1
        solution(i+1)
        s.pop()

solution(0)
print(count)
