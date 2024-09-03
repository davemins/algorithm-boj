'''
# 문제 이해
손상된 팀과 여분이 있는 팀의 정보를 통해 출발할 수 없는 팀 개수의 최솟값을 구하기

# 발상
손상된 팀의 정보와 여분이 있는 팀의 정보를 비교하면 될 것 같다

# 복잡도
손상된 팀의 수가 n이라고 했을 때 O(n)의 시간복잡도를 가진다.
근데 n이 20 이하여서 상관 안해도 괜찮을 것 같다.
'''

n, s, r = map(int, input().split())

damaged = list(map(int, input().split()))
onemore = list(map(int, input().split()))

# 리스트를 집합으로 변환하여 교집합을 찾고, 집합의 차집합으로 수정된 damaged와 onemore 리스트를 구합니다.
damaged_set = set(damaged)
onemore_set = set(onemore)
damaged = list(damaged_set - onemore_set)
onemore = list(onemore_set - damaged_set)

# damaged와 onemore를 다시 집합으로 변환하여 교차 테스트
damaged_set = set(damaged)
onemore_set = set(onemore)

result = 0
for i in damaged:
    if i - 1 in onemore_set:
        onemore_set.remove(i - 1)
    elif i + 1 in onemore_set:
        onemore_set.remove(i + 1)
    else:
        result += 1

print(result)

'''
# 푼 시간
30분

# 채점
오답

# 느낀 점
문제가 오답이 나올 때는 문제를 다시 읽어보는 것이 좋을 것 같다.
그라고 정답을 위한 변수를 하나 더 만드는 것이 좋아보인다.
또 런타임 오류가 날 때는 과정을 분리해보자.
'''