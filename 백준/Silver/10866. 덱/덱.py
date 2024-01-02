import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

exDeque = deque([])

for _ in range(N):
    command = list(input().split())

    if command[0] == 'push_back':
        exDeque.append(int(command[1]))
    elif command[0] == 'push_front':
        exDeque.appendleft(int(command[1]))
    elif command[0] == 'pop_back':
        if exDeque:
            print(exDeque.pop())
        elif not exDeque:
            print(-1)
    elif command[0] == 'pop_front':
        if exDeque:
            print(exDeque.popleft())
        elif not exDeque:
            print(-1)
    elif command[0] == 'size':
        print(len(exDeque))
    elif command[0] == 'empty':
        if exDeque:
            print(0)
        elif not exDeque:
            print(1)
    elif command[0] == 'front':
        if exDeque:
            print(exDeque[0])
        elif not exDeque:
            print(-1)
    elif command[0] == 'back':
        if exDeque:
            print(exDeque[-1])
        elif not exDeque:
            print(-1)
