import sys

input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    row = input().rstrip()
    if row not in arr:  # arr에 row와 같은 중복된 단어가 없으면 append
        arr.append(row)

arr.sort(key=lambda x:(len(x), x))

print('\n'.join(map(str, arr)))