import sys

arr = sys.stdin.readlines()
num = []

for line in arr:
    for i in line.strip().split():
        num.append(int(i[::-1]))

num = num[1:]
num.sort()
print("\n".join(map(str, num)))