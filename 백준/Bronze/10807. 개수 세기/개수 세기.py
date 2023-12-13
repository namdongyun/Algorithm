n = int(input())  # 수열의 크기 n
numList = list(map(int, input().split()))  # 수열에 포함되는 수
findNum = int(input())

print(numList.count(findNum))