import sys

input = sys.stdin.readline


def check_solution(visited, y, x):    # 7명의 학생이 붙어있는지 확인
    global check
    global student_count    # 붙어있는 학생 수

    visited[y][x] = False
    student_count += 1    # 학생 카운트 +1

    if student_count == 7:    # 학생 카운트가 7일 경우 7명 학생이 서로 붙어있으므로 check True
        check = True
        return

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or ny >= 5 or nx < 0 or nx >= 5:  # 좌표를 벗어난 경우 continue
            continue
        if not visited[ny][nx]:     # 학생이 없는 좌표인 경우 continue
            continue

        check_solution(visited, ny, nx)


def dfs(start, y_count, depth):
    global check
    global result
    global student_count

    if y_count >= 4:    # 임도연파가 4이상이면 반환
        return

    if depth == 7:  # 7명 뽑았으면
        visited = [[False] * 5 for _ in range(5)]
        for i in arr:
            visited[i[0]][i[1]] = True

        check_solution(visited, arr[0][0], arr[0][1])
        if check:
            check = False   # check 초기화
            result += 1
            
        student_count = 0   # 붙어있는 학생 수 초기화
        return

    for i in range(start, 25):
        y = i // 5   # y 좌표
        x = i % 5    # x 좌표
        arr.append((y, x))    # 탐색 좌표 추가
        dfs(i + 1, y_count + (graph[y][x] == 'Y'), depth + 1)
        arr.pop()   # 탐색 후 제거


graph = [list(input().rstrip()) for _ in range(5)]
arr = []

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

check = False
student_count = 0   # 붙어있는 학생 수
result = 0
dfs(0, 0, 0)
print(result)
