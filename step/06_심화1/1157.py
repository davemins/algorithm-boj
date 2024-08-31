"""단어 공부"""

word = input().lower()
word_list = list(set(word))
bag = []

for i in word_list:
    count = word.count(i)
    bag.append(count)

if bag.count(max(bag)) >= 2:
    print("?")
else:
    print(word_list[(bag.index(max(bag)))].upper())