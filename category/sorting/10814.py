'''
# 문제 이해
나이순으로 정렬해보자.

# 발상
튜플을 사용하자.

# 복잡도
데이터의 개수가 n이라고 할 때, O(nlongn)의 시간복잡도를 가진다.
이제 정렬 라이브러리의 시간복잡도도 고려하고자 한다.
'''

n = int(input())

data = []

for i in range(n):
    age, name = input().split()
    data.append((int(age), name))

def setting(data):
    return data[0]

result = sorted(data, key=setting)

for i in range(n):
    print(result[i][0], end=' ')
    print(result[i][1])

'''
# 푼 시간
10분 30초

# 채점
정답

# 느낀 점
정렬 라이브러리를 사용하니까 편하다.
병합 정렬 기반으로 만들어졌다고 하는데 어떤 정렬 방법인지 확인해보자.
'''