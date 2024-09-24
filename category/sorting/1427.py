'''
# 문제 이해
각 자릿수를 내림차순으로 정렬한 값을 출력

# 발상
정렬

# 복잡도
입력값의 길이를 n이라고 할 떄 O(n)의 시간복잡도를 가진다.

'''

number = input()

numbers = []

for i in range(len(number)):
    numbers.append(number[i])

numbers.sort(reverse = True)

result = ''

for j in range(len(numbers)):
    result += str(numbers[j])

print(result)

'''
# 푼 시간
6분 30초

# 채점
정답

# 느낀 점
감사하다.
'''