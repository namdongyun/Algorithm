import sys
from collections import deque

input = sys.stdin.readline

bracket = list(input().rstrip())  # 괄호

stack = deque([])

count = 0

for i in range(len(bracket)):

    if bracket[i] == '(':
        stack.appendleft(bracket[i])

    elif bracket[i] == ')':

        if stack and stack[0] == '(':

            if i >= 1 and bracket[i - 1] == '(':
                stack.popleft()
                count += len(stack)
            else:
                stack.popleft()
                count += 1

        elif stack and stack[0] == ')':
            stack.appendleft(bracket[i])

print(count)