'''
# 문제 이해
곱하자

# 발상
구현

# 복잡도
입력값 n, k에 대해 O(n*k)의 시간복잡도를 가진다.

'''
t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())

    # Initialize the ground floor (k = 0)
    array = [i + 1 for i in range(n)]

    # Fill in the rest of the floors
    for floor in range(1, k + 1):
        for apartment in range(1, n):
            array[apartment] += array[apartment - 1]

    # The answer is the number of people in the k-th floor and n-th apartment
    print(array[n - 1])
'''
# 푼 시간
30분

# 채점
오답

# 느낀 점
만만하게 보고 대충 풀려고 하면 무조건 틀리는 것 같다
'''