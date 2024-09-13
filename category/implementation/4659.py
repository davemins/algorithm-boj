'''
# 문제 이해
검사하여 조건이 맞는지 확인

# 발상
분기문으로 처리

# 복잡도
많음

'''


data = input()

aeiou = ['a', 'e', 'i', 'o', 'u']

while data != 'end':
    if len(data) == 1:
        if data in aeiou:
            print(f"<{data}> is acceptable.")
        else:
            print(f"<{data}> is not acceptable.")
    elif len(data) == 2:
        if data[0] == data[1] and data[0] not in ['e', 'o']:
            print(f"<{data}> is not acceptable.")
        elif all(vowel not in data for vowel in aeiou):
            print(f"<{data}> is not acceptable.")
        else:
            print(f"<{data}> is acceptable.")
    else:
        if all(vowel not in data for vowel in aeiou):
            print(f"<{data}> is not acceptable.")
        else:
            acceptable = True
            for i in range(1, len(data)):
                if data[i] == data[i - 1] and data[i] not in ['e', 'o']:
                    acceptable = False
                    break
                if i >= 2:
                    if (data[i - 2] in aeiou and data[i - 1] in aeiou and data[i] in aeiou) or \
                       (data[i - 2] not in aeiou and data[i - 1] not in aeiou and data[i] not in aeiou):
                        acceptable = False
                        break
            if acceptable:
                print(f"<{data}> is acceptable.")
            else:
                print(f"<{data}> is not acceptable.")
    data = input()



'''
# 푼 시간
30분

# 채점
오답

# 느낀 점
분기가 많을 수록 골이 아프다..
acceptable을 만들 걸 그랬다.
이번에 방법 하나 배워간다.
하여간 구현을 잘 못 풀고 있는 게 맞다. ㅠㅠ
'''