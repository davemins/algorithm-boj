# 시험 본 과목 개수 입력
N = int(input())

# 새로운 성적 저장 리스트
new_score = []

# 현재 성적 리스트로 입력 받아 가장 높은 값 저장
score = list(map(int, input().split()))
highest = max(score)

# 가장 높은 숫자로 새로운 성적 계산
for i in score:
    new = i / highest * 100
    new_score.append(new)

# 새로운 성적 평균 출력
print(sum(new_score)/N)