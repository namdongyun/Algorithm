import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())    # A의 수 N과 B의 수 M
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    result = 0
    start = 0

    for a in range(N):
        while True:
            if start == M or A[a] <= B[start]:
                break
            else:
                start += 1
        result += start

    print(result)
