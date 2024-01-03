import sys

input = sys.stdin.readline

while True:
    strList = input().rstrip('\n')
    stack = []

    if strList == ".":    # 입력의 종료조건으로 맨 마지막에 온점 하나(".")가 들어온다.
        break

    for i in strList:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
                break
    if len(stack) != 0:
        print('no')
    else:
        print('yes')
