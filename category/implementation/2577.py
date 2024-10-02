'''
# 문제 이해
곱한 수의 각 자릿수의 값들을 확인

# 발상
구현

# 복잡도
O(1)의 시간복잡도를 가진다.

'''
number = 1
array = [0] * 10
for _ in range(3):
    number *= int(input())

number_str = str(number)


for i in range(len(number_str)):
    array[int(number_str[i])] += 1

for j in range(10):
    print(array[j])
'''
# 푼 시간
4분

# 채점
정답

# 느낀 점
없습니다.
'''