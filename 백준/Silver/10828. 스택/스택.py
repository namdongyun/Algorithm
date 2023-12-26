import sys

input = sys.stdin.readline

commandNum = int(input())
stack = []

for i in range(commandNum):
    command = list(input().split())

    if command[0] == 'push':
        stack.append(int(command[1]))

    elif command[0] == 'pop':
        if not stack:
            print(-1)
        elif stack:
            print(stack.pop())

    elif command[0] == 'size':
        print(len(stack))

    elif command[0] == 'empty':
        if not stack:
            print(1)
        elif stack:
            print(0)

    elif command[0] == 'top':
        if not stack:
            print(-1)
        elif stack:
            print(stack[-1])



