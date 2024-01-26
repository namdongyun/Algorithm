import sys

input = sys.stdin.readline

N = int(input().rstrip())


def solution(n):
    if n == 1:
        return ['*']

    Stars = solution(n//3)
    L = []

    for S in Stars:
        L.append(S*3)
    for S in Stars:
        L.append(S + ' '*(n//3) + S)
    for S in Stars:
        L.append(S*3)

    return L

print('\n'.join(solution(N)))

