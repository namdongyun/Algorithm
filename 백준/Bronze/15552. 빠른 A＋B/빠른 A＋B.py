import sys

count = int(sys.stdin.readline())

for _ in range(count):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)