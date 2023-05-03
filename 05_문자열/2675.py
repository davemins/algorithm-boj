"""문자열 반복"""

amount = int(input())

count = []
word = []

for n in range(amount):
    count_element, word_element = map(str, input().split())
    count.append(int(count_element))
    word.append(word_element)

for i in range(amount):
    length = len(word[i])
    for j in range(length):
        for m in range(count[i]):
            print(word[i][j], end="")
    print("")