import sys

input = sys.stdin.readline

N = int(input())
arr = set([input().rstrip() for _ in range(N)])

arr = sorted(arr, key=lambda x:(len(x), x))

print('\n'.join(map(str, arr)))