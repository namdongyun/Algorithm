res = ['D', 'C', 'B', 'A', 'E']

for _ in range(3):
    print(res[sum(list(map(int, input().split())))])