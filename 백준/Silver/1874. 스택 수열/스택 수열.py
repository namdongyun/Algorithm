import sys

input = sys.stdin.readline

n = int(input())

stack = []
result = []
current = 0

for i in range(n):
    num = int(input())

    while current < num:
        current += 1
        stack.append(current)
        result.append('+')

        if current == num:
            stack.pop()
            result.append('-')
            continue


    if current > num:

        if stack[-1] == num:
            stack.pop()
            result.append('-')
        elif stack[-1] != num:
            result.append(-1)
            break

if result[-1] == -1:
    print('NO')
else:
    for i in range(len(result)):
        print(result[i])
