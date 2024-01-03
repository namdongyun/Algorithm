import sys
from collections import deque

input = sys.stdin.readline

T = int(input())    # 테스트 케이스의 개수 T

for _ in range(T):
    p = list(input().strip())   # 수행할 함수 p
    n = int(input())            # 배열에 들어있는 수의 개수 n

    numList = input().strip()   # 정수가 들어가 있는 배열이 주어짐
    
    if n == 0:                  # 배열에 들어있는 수가 없다면
        dq = deque()            # 빈 deque 생성
    else:
        dq = deque(numList[1:-1].split(','))

    R = 0   # 뒤집는 횟수 (짝수이면 의미없으므로 뒤집지 않기 위해)

    for i in range(len(p)):
        if p[i] == 'R':
            R += 1
        elif p[i] == 'D':
            if not dq:
                print("error")
                break
            elif dq:
                if R % 2 == 0:
                    dq.popleft()
                else:
                    dq.pop()

    else:   # break 없이 루프가 정상적으로 종료되었을 때만
        if R % 2 == 0:
            print('[' + ','.join(dq) + ']')
        else:
            dq.reverse()
            print('[' + ','.join(dq) + ']')

