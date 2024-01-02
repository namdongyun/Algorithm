import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
exQueue = deque([])

for i in range(1, N+1):
    exQueue.append(i)

while len(exQueue) > 1:
    exQueue.popleft()
    exQueue.append(exQueue.popleft())

print(exQueue.pop())