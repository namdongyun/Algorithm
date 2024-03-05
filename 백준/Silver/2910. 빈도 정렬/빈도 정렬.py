import sys

input = sys.stdin.readline

N, C = map(int, input().split())    # 메시지의 길이 N과 C, 숫자는 모두 C보다 작거나 같다
num = list(map(int, input().split()))

count = {}
index = 1

for n in num:
    if n in count:
        count[n][0] += 1    # 해당 숫자의 빈도수 +1
    else:
        count[n] = [1, index]   # n이 count에 없는 수라면 빈도수 1, 인덱스를 추가해줌
        index += 1  # 다음 수를 위해 index값 +1

numbers = [[i, j] for i, j in count.items()]    # [요소, [발생 횟수, 인덱스]] 형태 리스트로 변환
numbers.sort(key=lambda x:(-x[1][0], x[1][1]))   # x[1][0] : 발생 횟수 내림차순, x[1][1] : 인덱스 오름차순

res = []
for i, j in numbers:
    res += ([i] * j[0])  # i : 요소, j[0] : 발생 횟수

print(' '.join(map(str, res)))