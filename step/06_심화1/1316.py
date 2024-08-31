"""그룹 단어 체커"""

test_case = int(input())
count = test_case

for _ in range(test_case):
    word = input()
    word_box = [word[0]]
    for i in range(1, len(word)):
        if (word[i - 1] != word[i]) and (word[i] in word_box):
            count -= 1
            break
        word_box.append(word[i])

print(count)