import sys

input = sys.stdin.readline

L, C = map(int, input().split())
s = list(map(str, input().split()))
s.sort()
l = []  # 알파벳 조합 리스트

vowels = ['a', 'e', 'i', 'o', 'u']

def solution(start):
    if len(l) == L:
        vo, co = 0, 0

        for j in l:
            if j in vowels:
                vo += 1
            else:
                co += 1
        if vo >= 1 and co >= 2:
            print(''.join(l))
        return
    for i in range(start, C):
        l.append(s[i])
        solution(i+1)
        l.pop()

solution(0)