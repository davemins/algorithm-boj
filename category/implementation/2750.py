'''
# 문제 이해
입력값을 오름차순으로 출력하자.

# 발상
구현

# 복잡도
입력 숫자의 개수가 n개일 때 O(n)의 시간복잡도를 가진다.

'''
n = int(input())

numbers = []

for i in range(n):
    numbers.append(int(input()))

numbers.sort()

for j in range(n):
    print(numbers[j])
'''
# 푼 시간
3분

# 채점
정답

# 느낀 점
없습니다.
'''