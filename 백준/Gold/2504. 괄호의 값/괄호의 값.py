import sys
from collections import deque

input = sys.stdin.readline


def solution():
    bracket = list(input().rstrip())

    stack = deque()
    num = 1
    result = 0

    for i in range(len(bracket)):
        if bracket[i] == '(':
            stack.appendleft(bracket[i])
            num *= 2

        elif bracket[i] == '[':
            stack.appendleft(bracket[i])
            num *= 3

        elif bracket[i] == ')':
            if not stack or stack[0] != '(':
                return 0
            if i >= 1 and bracket[i - 1] == '(':
                result += num
            stack.popleft()
            num //= 2

        elif bracket[i] == ']':
            if not stack or stack[0] != '[':
                return 0
            if i >= 1 and bracket[i - 1] == '[':
                result += num
            stack.popleft()
            num //= 3

    if stack:
        return 0
    
    return result


print(solution())
