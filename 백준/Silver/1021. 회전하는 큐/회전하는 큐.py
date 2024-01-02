import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())    # 큐의 크기 N,  뽑아내려고 하는 수의 개수 M

dq = deque([i for i in range(1, N+1)]) # deque 생성

positionList = list(map(int, input().split()))   # 뽑아내려고 하는 수의 위치

count = 0

for i in positionList:
    while True:
        if dq[0] == i:
            dq.popleft()
            break
        else:
            if dq.index(i) <= len(dq)/2:    # dq의 크기를 반으로 나누어 현재 찾는 i값이 있는 dq의 인덱스 위치와 비교함
                while dq[0] != i:           # dq에 있는 i값의 인덱스가 dq 크기보다 작거나 같으면 맨 앞 숫자를 뒤로 넘겨 i값을 구함
                    dq.rotate(-1)
                    count += 1
            else:
                while dq[0] != i:           # dq에 있는 i값의 인덱스가 dq 크기보다 크면 맨 뒤 숫자를 앞으로 넘겨서 i값을 구함
                    dq.rotate(1)
                    count += 1
print(count)
