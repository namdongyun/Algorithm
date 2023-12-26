import sys

input = sys.stdin.readline

K = int(input())
stack = []

for i in range(K):
    command = int(input())

    if command == 0:
        if not stack:
            continue
        elif stack:
            stack.pop()

    else:
        stack.append(command)

sumNum = 0
for i in range(len(stack)):
    sumNum += stack[i]

print(sumNum)