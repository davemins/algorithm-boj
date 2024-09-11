'''
# 문제 이해
문자열의 특성을 분석하여 재배열 하는 것

# 발상
검사해서 동일한 문자가 몇 개 있는지 조사하며 완전 탐색

# 복잡도
입력 문자열의 길이가 n일 때 O(n)의 시간복잡도를 가진다.
'''

str_input = input()

str_list = []

result_list = []

odd = ''

for i in range(len(str_input)):
    str_list.append(str_input[i])


for i in range(len(str_list)):
    if str_list[i] not in result_list:
        count = str_list.count(str_list[i])
        if count == 1:
            if odd != '':
                odd = str_list[i]
            else:
                odd += str_list[i]
        if count % 2 == 0:
            for j in range(count // 2):
                result_list.append(str_list[i])
        else:
            for j in range(count // 2):
                result_list.append(str_list[i])
                if odd != '':
                    odd = str_list[i]
                else:
                    odd += str_list[i]

result_list.sort()
result = ''

for i in result_list:
    result += i

if len(odd) == 0:
    for i in range(len(result_list) - 1, -1, -1):
        result += result_list[i]
    print(result)
elif len(odd) == 1:
    result += odd
    for i in range(len(result_list) - 1, -1, -1):
        result += result_list[i]
    print(result)
else:
    print("I'm Sorry Hansoo")
'''
# 푼 시간
33분

# 채점
오답

# 느낀 점
뭔가 되게 바쁘게 풀긴 했는데 왜 틀린지 모르겠다.
발상은 좋았는데 디테일을 자꾸 놓치는 것 같다.
'''
