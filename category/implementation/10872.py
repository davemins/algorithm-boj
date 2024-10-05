
'''
# 문제 이해
팩토리얼

# 발상
재귀 함수

# 복잡도
입력값이 n일 때 O(n)의 시간복잡도를 가진다.

'''
def factorial(n):
    result = 1
    if n > 0 :
        result = n * factorial(n-1)
    return result

n = int(input())
print(factorial(n))


'''
# 푼 시간
0분

# 채점
정답

# 느낀 점
없습니다.
'''