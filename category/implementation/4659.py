'''
# 문제 이해


# 발상


# 복잡도


'''


data = input()

aeiou = ['a', 'e', 'i', 'o', 'u']

while data != 'end':
    if len(data) == 1:
        if data == 'a' or data == 'e' or data == 'i' or data == 'o' or data == 'u':
            print("<" + data + ">" " is acceptable.")
        else:
            print("<" + data + ">" " is not acceptable.")
    elif len(data) == 2:
        if data[0] == data[1] and data[0] != 'e' and data[0] != 'o':
            print("<" + data + ">" " is not acceptable.")
        elif 'a' not in data or 'e' not in data or 'i' not in data or 'o' not in data or 'u' in data:
            print("<" + data + ">" " is not acceptable.")
        else:
            print("<" + data + ">" " is acceptable.")
    else:
        if 'a' not in data and 'e' not in data and 'i' not in data and 'o' not in data and 'u' in data:
            print("<" + data + ">" " is not acceptable.")
        else:
            for i in range(1, len(data)):
                if data[i] == data[i - 1] and data[i] != 'e' and data[i] != 'o':
                    print("<" + data + ">" " is not acceptable.")
                    break
                else:
                    if i >= 2:
                        if data[i - 2] in aeiou and data[i - 1] in aeiou and data[i] in aeiou:
                            print("<" + data + ">" " is not acceptable.")
                            break
                        elif data[i - 2] not in aeiou and data[i - 1] not in aeiou and data[i] not in aeiou:
                            print("<" + data + ">" " is not acceptable.")
                            break
                if i == len(data) - 1:
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