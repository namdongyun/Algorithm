import sys
from collections import deque

input = sys.stdin.readline

n, w, L = map(int, input().split())     # n: 트럭 수, w : 다리 길이, L, 다리 최대하중
data = list(map(int, input().split()))
graph = deque(data)     # 트럭 리스트
dq = deque()            # 다리 위에 있는 트럭 리스트
time = 0

while graph or dq:
    time += 1   # 시간 증가
    count = 0

    for i in range(len(dq)):    # 다리 위에 있는 트럭 리스트 w - 1
        dq[i][1] -= 1
        if dq[i][1] == 0:   # 트럭의 남은 다리 길이가 0 이면 dq에서 제거
            L += dq[i][0]   # 다리 최대 하중 + 나가는 트럭 무게
            count += 1      # 나가는 트럭 개수 저장
    for _ in range(count):  # 나가는 트럭 개수 만큼 popleft()
        dq.popleft()
        
    if graph:   # 남은 트럭이 있으면
        if L >= graph[0]:   # 들어올 트럭의 무게가 현재 다리 최대하중보다 작거나 같을 경우
            L -= graph[0]   # 다리 최대 하중 - 들어오는 트럭 무게
            dq.append([graph.popleft(), w])

print(time)
