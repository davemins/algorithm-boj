'''
# 문제 이해
최소 갯수의 3과 5로 만들 수 있는 조합

# 발상
동적계획법

# 복잡도
입력값이 n일 때 O(n)의 시간복잡도를 가진다.

'''
n = int(input())

dp_table = [-1] * (n + 1)

for i in range(3, n + 1):
    if i == 3:
        dp_table[i] = 1
    elif i == 5:
        dp_table[i] = 1
    else:
        if dp_table[i - 3] > 0 and dp_table[i - 5] > 0:
            dp_table[i] = min(dp_table[i - 3], dp_table[i - 5]) + 1
        elif dp_table[i - 3] <= 0 < dp_table[i - 5]:
            dp_table[i] = dp_table[i - 5] + 1
        elif dp_table[i - 3] > 0 >= dp_table[i - 5]:
            dp_table[i] = dp_table[i - 3] + 1

print(dp_table[n])


'''
# 푼 시간
14분

# 채점
정답

# 느낀 점
어떤 경우의 수가 나올 수 있는지 정확히 확인하자.
'''