'''
# 문제 이해
숫자 조합으로 만들 수 있는 경우의 수 구하기

# 발상
count_array[i] = count_array[i - 3] + count_array[i - 2] + count_array[i - 1]

# 복잡도
데이터의 개수가 n일 때 O(n)의 시간복잡도를 가진다.

'''

n = int(input())

number_array = []

for i in range(n):
    number_array.append(int(input()))

count_array = [0] * (max(number_array) + 1)

for i in range(1, max(number_array) + 1):
    if i == 1:
        count_array[i] = 1
    elif i == 2:
        count_array[i] = 2
    elif i == 3:
        count_array[i] = 4
    else:
        count_array[i] = count_array[i - 3] + count_array[i - 2] + count_array[i - 1]

for num in number_array:
    print(count_array[num])

'''
# 푼 시간
30분

# 채점
오답

# 느낀 점
점화식이 생각나지 않았었다.
아예 발상이 안되었음..
'''