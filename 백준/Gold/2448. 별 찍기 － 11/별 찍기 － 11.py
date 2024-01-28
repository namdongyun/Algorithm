import sys

input = sys.stdin.readline

N = int(input())

def solution(n):
    if n == 3:
        L = []
        L.append(' ' * 2 + '*' + ' ' * 2)
        L.append(' ' + '*' + ' ' + '*' + ' ')
        L.append('*' * 5)
        return L

    Stars = solution(n//2)
    L = []

    for S in Stars:
        L.append(' '*(n//2) + S + ' '*(n//2))
    for S in Stars:
        L.append(S + ' ' + S)

    return L


print('\n'.join(solution(N)))
