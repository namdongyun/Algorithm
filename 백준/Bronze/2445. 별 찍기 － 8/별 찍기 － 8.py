import sys

n = int(sys.stdin.readline())

for i in range(1, n+1):
    print('*'*i + ' '*(n-i) + ' '*(n-i) + '*'*i)

for i in range(1, n):
    print('*'*(n-i) + ' '*i + ' '*i + '*'*(n-i))