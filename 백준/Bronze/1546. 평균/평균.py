import sys

input = sys.stdin.readline

N = int(input())
grade = list(map(int, input().split()))

sumGrade = 0
maxGrade = 0

for i in grade:
    maxGrade = max(maxGrade, i)

for i in grade:
    sumGrade += i / maxGrade * 100

print(sumGrade/N)
