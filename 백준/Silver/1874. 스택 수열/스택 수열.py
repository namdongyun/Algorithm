import sys

input = sys.stdin.readline

n = int(input())

stack = []
result = []
current = 0

for i in range(n):
    num = int(input())

    while current < num:    # 입력한 num 이 current 보다 클 경우
        current += 1
        stack.append(current)   # current 값을 1씩 올리며 stack 에 넣어줌
        result.append('+')      # push 이므로 +

        if current == num:      # current 와 num 이 같으면
            stack.pop()         # pop 으로 숫자를 빼냄
            result.append('-')  # pop 이므로 -

    if current > num:   # 입력한 num 이 current 보다 작을 경우

        if stack[-1] == num:
            stack.pop()
            result.append('-')
        elif stack[-1] != num:  # 스택의 마지막 숫자가 입력한 num이 아니면 
            result.append(-1)   # result 의 마지막 인덱스에 -1을 추가
            break

if result[-1] == -1:    # result 의 마지막 인덱스가 -1이면 NO 출력
    print('NO')
else:
    for i in range(len(result)):
        print(result[i])
