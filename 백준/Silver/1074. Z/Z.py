import sys

input = sys.stdin.readline

N, r, c = map(int, input().split())

cnt = 0

while N > 1:
    size = (2 ** N) // 2

    if r < size and c < size:           # 2사분면
        pass
    elif r < size and c >= size:        # 1사분면
        cnt += size**2              # 모든 값에 + size**2
        c -= size                   # x 좌표를 size 만큼 빼줌

    elif r >= size and c < size:        # 3사분면
        cnt += size**2 * 2          # 모든 값에 + size**2 * 2
        r -= size                   # y 좌표를 size 만큼 빼줌

    elif r >= size and c >= size:       # 4사분면
        cnt += size**2 * 3          # 모든 값에 + size**2 * 3
        r -= size                   # y 좌표를 size 만큼 빼줌
        c -= size                   # x 좌표를 size 만큼 빼줌

    N -= 1

if r == 0 and c == 0:
    print(cnt)
elif r == 0 and c == 1:
    print(cnt + 1)
elif r == 1 and c == 0:
    print(cnt + 2)
elif r == 1 and c == 1:
    print(cnt + 3)

