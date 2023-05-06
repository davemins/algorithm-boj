"""팰린드롬인지 확인하기"""

word = input()
tmp = []

for i in range(len(word)):
    tmp.append(word[i])

mount = len(word) // 2
count = 1

for j in range(mount):
    if tmp[j] == tmp[len(word) - j - 1]:
        if count == mount:
            print("1")
        count += 1
    else:
        print("0")
        break