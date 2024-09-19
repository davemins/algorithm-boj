'''
# 문제 이해
제곱한 것을 더한 후 나머지를 구하자.

# 발상
구현 잘하자.

# 복잡도
데이터의 개수가 n개일 때 O(n)의 시간복잡도를 가진다.

'''

data = map(int, input().split())

square_sum = 0

for i in data:
    square_sum += i * i

result = square_sum % 10

print(result)
'''
# 푼 시간
2분 30초

# 채점
정답

# 느낀 점
없습니다.
'''