import sys

n = int(sys.stdin.readline())

for i in range(n):
    print(' '*(n-(i+1)) + '*'*((i+1)*2-1))

for i in range(n-1):
    print(' '*(i+1) + '*'*(2*((n-1)-i)-1))