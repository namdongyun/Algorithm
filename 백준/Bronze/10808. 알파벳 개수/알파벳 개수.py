word = input()

al = [0]*26

for i in word:
    al[ord(i)-97] += 1

for i in al:
    print(i, end=" ")