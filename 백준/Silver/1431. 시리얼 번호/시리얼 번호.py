import sys

input = sys.stdin.readline

N = int(input())    # 기타의 개수
serial = [input().rstrip() for _ in range(N)]


def sum_num(serialNum):
    result = 0
    for i in serialNum:
        if i.isdigit():
            result += int(i)
    return result


serial.sort(key=lambda x:(len(x), sum_num(x), x))

for i in serial:
    print(i)