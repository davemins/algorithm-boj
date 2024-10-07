'''
# 문제 이해
다리 최대로 놓을 수 있는 경우의 수

# 발상
조합

# 복잡도
엄청 많다

'''
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

n = int(input())

result_list = []

for i in range(n):
    a, b = map(int, input().split())
    result_list.append(factorial(b) // (factorial(a) * factorial(b - a)))

for j in range(n):
    print(result_list[j])

'''
# 푼 시간
30분

# 채점
오답

# 느낀 점
조합을 활용해야 한다는 것까지는 발상이 가능했다.
그러나 팩토리얼 구현과 조합 구현에서 시간을 넘었다.
그리고 조합 구현도 하나 빼먹어서 틀렸다..
'''