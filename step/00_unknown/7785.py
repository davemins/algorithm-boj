"""회사에 있는 사람"""

# 사람 명수 입력
n = int(input())
people = dict()

# 이름과 상태 입력
for i in range(n):
    name, status = map(str, input().split())
    if status == 'enter':
        people[name] = status
    else:
        del people[name]

for k in sorted(people.keys(), reverse=True):
    print(k)