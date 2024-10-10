'''
# 문제 이해
별찍기

# 발상
구현

# 복잡도
입력값이 n일 때 O(n)의 시간복잡도를 가진다.

'''
n = int(input())

for i in range(n, 0, -1):
    print(' ' * (n - i), end='')
    print('*' * (2 * i - 1))

for j in range(2, n + 1):
    print(' ' * (n - j), end='')
    print('*' * (2 * j - 1))

'''
# 푼 시간
5분

# 채점
정답

# 느낀 점
없습니다.
'''