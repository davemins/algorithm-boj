'''
# 문제 이해
덩치가 큰 사람의 명수를 찾으면 된다.

# 발상
일단은 입력부터 받자.
그리고 비교하자.

# 복잡도
사람의 수를 n이라고 할 때 O(n^2)의 시간복잡도를 가진다.
n 의 최대값은 50이기에 문제가 될 것 같지는 않다.
'''
n = int(input())

data = []

result = [1 for _ in range(n)]

for i in range(n):
    data.append(list(map(int, input().split())))

for j in range(n):
    for i in range(n):
        if data[j][0] < data[i][0] and data[j][1] < data[i][1]:
            result[j] += 1

for i in range(n):
    print(result[i], end=' ')
'''
# 푼 시간
12분

# 채점
정답

# 느낀 점
구현이 생각보다 쉬운 카테고리는 아닌 것 같다.
그나마 쉬운 문제를 찾다가 이 문제를 발견했다.
더 어려운 문제도 차근차근 연습해보자.
'''