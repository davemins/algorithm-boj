'''
# 문제 이해
1로 만들기 위한 최적의 방법 횟수를 구하자.

# 발상
가장 최적의 횟수를 찾아야 하므로 그 전 단계의 값들을 비교하면 정확히 찾을 수 있다.

# 복잡도
입력값을 n이라고 할 때 O(n)의 시간복잡도를 가진다.

'''
n = int(input())
count = 0

dp_table = [0] * (n + 1)


for i in range(1, n + 1):
    if i == 1:
        dp_table[i] = 0
    elif i == 2:
        dp_table[i] = 1
    elif i == 3:
        dp_table[i] = 1
    else:
        if i % 2 == 0 and i % 3 == 0:
            dp_table[i] = min(dp_table[i - 1], dp_table[i // 3], dp_table[i // 2]) + 1
        elif i % 2 == 0 and i % 3 != 0:
            dp_table[i] = min(dp_table[i - 1], dp_table[i // 2]) + 1
        elif i % 2 != 0 and i % 3 == 0:
            dp_table[i] = min(dp_table[i - 1], dp_table[i // 3]) + 1
        else:
            dp_table[i] = dp_table[i - 1] + 1

print(dp_table[n])

'''
# 푼 시간
22분

# 채점
정답

# 느낀 점
중간에 실수를 많이 했다.
i를 n으로 쓰기도 하고, 디버깅용 프린트문도 지우지 않았었다.
그리고 이게 동적 계획법이라는 근거를 내가 찾을 수 있을까는 미지수다.
그래도 맞춰서 기분이 좋다.
'''