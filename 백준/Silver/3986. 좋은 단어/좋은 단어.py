import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

count = 0

for i in range(N):
    word = input().rstrip()
    stack = deque([])

    for j in range(len(word)):
        if stack and word[j] == stack[0]:     # stack에 처음 값과 스택에 넣을려는 값이 일치하면 pop
            stack.popleft()
        else:
            stack.appendleft(word[j])

    if not stack:
        count += 1

print(count)




