import sys

input = sys.stdin.readline

N = int(input())    # 테스트 케이스 개수

for _ in range(N):  # 테스트 케이스 개수 만큼 반복
    inputStr = list(input().rstrip())   # 테스트 케이스 문자열 받기

    str1 = []
    str2 = []

    for i in range(len(inputStr)):
        if inputStr[i] == '<':          # < 일때 str2 맨뒤에 str1 맨뒤 문자 추가
            if str1:
                str2.append(str1.pop())

        elif inputStr[i] == '>':        # > 일때 str1 맨뒤에 str2 맨뒤 문자 추가
            if str2:
                str1.append(str2.pop())

        elif inputStr[i] == '-':        # - 일때 str1 맨뒤 문자 제거
            if str1:
                str1.pop()
        
        else:
            str1.append(inputStr[i])    # str1 맨뒤에 문자 추가

    str1.extend(reversed(str2))
    print("".join(str1))


