import re
import sys

input = sys.stdin.readline

N = int(input())    # 기타의 개수
serial = [input().rstrip() for _ in range(N)]


for i in range(N - 1):
    for j in range(i + 1, N):
        if len(serial[i]) > len(serial[j]):       # 뒤에 시리얼번호 길이가 더 짧으면 서로 자리 바꿈
            tmp = serial[i]
            serial[i] = serial[j]
            serial[j] = tmp
        elif len(serial[i]) == len(serial[j]):   # 두 시리얼번호 길이가 같으면
            aNum = re.findall(r'\d', serial[i])
            bNum = re.findall(r'\d', serial[j])

            aSum, bSum = 0, 0

            for n in aNum:
                aSum += int(n)
            for n in bNum:
                bSum += int(n)

            if aSum > bSum:     # A의 모든 자리수의 합과 B의 모든 자리수의 합을 비교해서 작은 합을 가지는 것이 먼저온다
                tmp = serial[i]
                serial[i] = serial[j]
                serial[j] = tmp
            elif aSum == bSum:   # 비교 불가
                if serial[i] > serial[j]:
                    tmp = serial[i]
                    serial[i] = serial[j]
                    serial[j] = tmp

for i in serial:
    print(i)