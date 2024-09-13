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
odd_count = 0  # 홀수 개수 문자의 수를 셀 변수

# 문자열을 리스트에 저장
for i in range(len(str_input)):
    str_list.append(str_input[i])

# 문자의 개수를 세고 팰린드롬을 만들 수 있는지 확인
for char in set(str_list):  # 중복을 피하기 위해 set 사용
    count = str_list.count(char)
    if count % 2 == 1:  # 홀수인 경우
        odd_count += 1
        odd = char  # 홀수인 문자를 odd에 저장 (최대 하나)
        if odd_count > 1:  # 홀수인 문자가 2개 이상이면 팰린드롬 불가
            print("I'm Sorry Hansoo")
            exit()
    result_list.extend([char] * (count // 2))  # 절반만큼 추가

# 팰린드롬을 만들 수 있는 경우
result_list.sort()  # 팰린드롬의 첫 번째 절반 정렬
result = ''.join(result_list)  # 첫 번째 절반 문자열

# 팰린드롬의 완성을 위해 중앙에 odd 문자를 넣고, 뒤집은 절반 추가
if odd_count == 1:
    result += odd  # 가운데에 홀수 문자를 추가

result += ''.join(reversed(result_list))  # 뒤집은 절반 추가

print(result)

'''
# 푼 시간
33분

# 채점
오답

# 느낀 점
뭔가 되게 바쁘게 풀긴 했는데 왜 틀린지 모르겠다.
발상은 좋았는데 디테일을 자꾸 놓치는 것 같다.

join 배워간다.
'''
