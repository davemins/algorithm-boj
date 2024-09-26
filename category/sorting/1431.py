'''
# 문제 이해
세가지 조건으로 문자열들을 정렬해보자.

# 발상
데이터의 최대 갯수가 50이므로 계수 정렬을 사용하면 좋을 것 같아.

# 복잡도
데이터의 개수가 n이라고 할 때 O(n)의 시간복잡도를 가진다.


'''
n = int(input())
data_location = [[] for _ in range(51)]

for i in range(n):
    number = input()
    data_location[len(number)].append(number)

def set_by_sum(data):
    number_sum = 0
    for j in range(len(data)):
        if data[j].isdigit():  # 숫자인지 확인
            number_sum += int(data[j])
    return number_sum

# 길이별로 정렬 (자리수 합 -> 사전순)
for i in range(51):
    if len(data_location[i]) > 1:
        data_location[i] = sorted(data_location[i], key=lambda x: (set_by_sum(x), x))

# 한 줄에 하나씩 출력
for i in range(51):
    if data_location[i]:
        for number in data_location[i]:
            print(number)

'''
# 푼 시간
30분

# 채점
오답

# 느낀 점
생각보다 어렵다..
두 번째 조건까지는 반영되었는데, 세 번째는 람다를 사용해서 하는 방법을 몰랐었다.
다음에는 맞춰보자.
'''