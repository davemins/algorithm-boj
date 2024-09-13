'''
# 문제 이해


# 발상


# 복잡도


'''

data = input()

aeiou = ['a', 'e', 'i', 'o', 'u']

while data != 'end':
    if 'a' not in data and 'e' not in data and 'i' not in data and 'o' not in data and 'u' in data:
        print("<" + data + ">" " is not acceptable.")
    else:
        for i in range(1, len(data)):
            if data[i] == data[i-1] and data[i] != 'e' and data[i] != 'o':
                print("<" + data + ">" " is not acceptable.")
                break
            else:
                if i >= 2:
                    if data[i-2] in aeiou and data[i-1] in aeiou and data[i-2] in aeiou:
                        print("<" + data + ">" " is not acceptable.")
                        break
                    elif data[i - 2] not in aeiou and data[i - 1] not in aeiou and data[i - 2] not in aeiou:
                        print("<" + data + ">" " is not acceptable.")
                        break
            if i == len(data) - 1:
                print("<" + data + ">" " is acceptable.")

    if data == 'a' or data == 'e' or data == 'i' or data == 'o' or data == 'u':
        print("<" + data + ">" " is acceptable.")

    data = input()


'''
# 푼 시간
30분

# 채점
오답

# 느낀 점
분기가 많을 수록 골이 아프다..


'''