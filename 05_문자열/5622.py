"""다이얼"""

word = input()
total_elapsed_second = 0

for i in range(len(word)):

    if word[i] == 'A' or word[i] == 'B' or word[i] == 'C':
        total_elapsed_second += 3
    elif  word[i] == 'D' or word[i] == 'E' or word[i] == 'F':
        total_elapsed_second += 4
    elif  word[i] == 'G' or word[i] == 'H' or word[i] == 'I':
        total_elapsed_second += 5
    elif  word[i] == 'J' or word[i] == 'K' or word[i] == 'L':
        total_elapsed_second += 6
    elif  word[i] == 'M' or word[i] == 'N' or word[i] == 'O':
        total_elapsed_second += 7
    elif  word[i] == 'P' or word[i] == 'Q' or word[i] == 'R' or word[i] == 'S':
        total_elapsed_second += 8
    elif  word[i] == 'T' or word[i] == 'U' or word[i] == 'V':
        total_elapsed_second += 9
    elif  word[i] == 'W' or word[i] == 'X' or word[i] == 'Y' or word[i] == 'Z':
        total_elapsed_second += 10

print(total_elapsed_second)