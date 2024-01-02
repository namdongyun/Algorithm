import sys

input = sys.stdin.readline

N = int(input())
exQueue = []

for _ in range(N):
    command = list(input().split())

    if command[0] == 'push':
        exQueue.append(int(command[1]))
    elif command[0] == 'pop':
        if exQueue:
            print(exQueue.pop(0))
        elif not exQueue:
            print(-1)
    elif command[0] == 'size':
        print(len(exQueue))
    elif command[0] == 'empty':
        if exQueue:
            print(0)
        elif not exQueue:
            print(1)
    elif command[0] == 'front':
        if exQueue:
            print(exQueue[0])
        elif not exQueue:
            print(-1)
    elif command[0] == 'back':
        if exQueue:
            print(exQueue[-1])
        elif not exQueue:
            print(-1)
