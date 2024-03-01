import sys

input = sys.stdin.readline

N = int(input())
graph = [[0 for _ in range(N+1)]]

for _ in range(N):
    row = [0] + list(map(int, input().split()))
    graph.append(row)

team1 = []
team2 = []

minResult = 99999


def solution(depth, start, team1, team2):
    global minResult
    team1_ability = 0
    team2_ability = 0

    if depth == N//2:
        team2 = []
        for k in range(1, N+1):     # team1에 속하지 않는 나머지를 team2에 넣기
            if k not in team1:
                team2.append(k)

        for i in range(N//2):       # team1 배열 인덱스
            for j in range(i+1, N//2):
                team1_ability += graph[team1[i]][team1[j]] + graph[team1[j]][team1[i]]

        for i in range(N//2):       # team1 배열 인덱스
            for j in range(i+1, N//2):
                team2_ability += graph[team2[i]][team2[j]] + graph[team2[j]][team2[i]]

        minResult = min(minResult, abs(team1_ability - team2_ability))
        return

    for i in range(start, N+1):     # 사람 start번 ~ N번까지
        team1.append(i)
        solution(depth + 1, i + 1, team1, team2)
        team1.pop()
            

# depth : team1에 사람을 뽑는 횟수
# start : # 사람 start번 ~ N번까지 뽑기
solution(0, 1, team1, team2)
print(minResult)
