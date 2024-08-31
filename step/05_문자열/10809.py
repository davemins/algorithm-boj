"""알파벳 찾기"""

import string

def listAlphabet():
    return list(string.ascii_lowercase)

word = input()

for i in listAlphabet():
    if i in word:
        number = word.find(i)
        print(number, end=" ")
    else:
        print(-1, end=" ")