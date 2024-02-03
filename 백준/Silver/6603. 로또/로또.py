import sys

input = sys.stdin.readline

l = []  # 6개의 숫자 조합 리스트

def solution(k, s, start):
    if len(l) >= 6:
        print(' '.join(map(str, l)))
        return
    for i in range(start, k):
        l.append(s[i])
        solution(k, s, i+1)
        l.pop()



while True:
    input_str = list(map(int, input().split()))

    if input_str[0] == 0:
        break

    k = input_str[0]    # 입력 받은 리스트의 수
    s = list(map(int, input_str[1:]))   # 입력 받은 리스트

    solution(k, s, 0)
    print() # 테스트케이스 이후 한칸 띄기