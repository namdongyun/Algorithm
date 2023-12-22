import sys

input = sys.stdin.readline

str1 = list(input().rstrip())    # 커서 왼쪽 리스트
str2 = []               # 커서 오른쪽 리스트

M = int(input())        # 시행 할 횟수

for _ in range(M):
    command = list(input().split())
    if command[0] == 'L' and str1:      # 커서 왼쪽 리스트가 없으면 무시됨
        str2.append(str1.pop())

    elif command[0] == 'D' and str2:
        str1.append(str2.pop())

    elif command[0] == 'B' and str1:
        str1.pop()

    elif command[0] == 'P':
        str1.append(command[1])

str1.extend(reversed(str2))
print("".join(str1))
