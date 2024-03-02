import sys

input = sys.stdin.readline


def check(num_list, re_num_list):
    for i in range(len(num_list)):
        if num_list[i] != re_num_list[i]:
            return False
    return True


while True:
    num = str(input().rstrip())

    if num == '0':
        break

    num_list = list(num)
    re_num_list = list(reversed(num_list))

    if check(num_list, re_num_list):
        print('yes')
    else:
        print('no')