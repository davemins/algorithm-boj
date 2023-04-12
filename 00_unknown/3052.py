"""나머지"""

# 나머지 저장 리스트
rest = []

# 숫자 10개 입력받은 후 나머지 저장
for i in range(10):
    rest.append(int(input())%42)

# 중복 제거 후 출력
rest = set(rest)
print(len(rest))