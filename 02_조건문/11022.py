"""A+B-8"""

# 테스트 케이스 개수 T 입력
T = int(input())

# 저장 리스트 선언
store = []

# 테스트 케이스 개수만큼 숫자 2개 입력받아 저장
for i in range(T):
    store.append(input())

# 입력받은 수를 a, b로 나누어 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력
for i in range(T):
    a, b = map(int, store[i].split())
    print('Case #{}: {} + {} = {}'.format(i+1, a, b, a + b))