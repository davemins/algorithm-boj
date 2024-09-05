'''
# 문제 이해
주어진 수 n에 구성된 숫자로 만들 수 있는 30의 배수 중 최대값을 구하기
만들 수 없으면 -1 출력하기

# 발상
30의 배수를 써보며 특징을 살펴보자.

# 복잡도
양수의 구성 숫자의 개수를 n이라고 할 때 O(2n)의 시간복잡도를 가진다.
최대 10^5개의 숫자로 구성되어 있으므로 시간복잡도는 문제 없을 듯 하다.

'''
n = input()

n_list = []
for i in range(len(n)):
    n_list.append(n[i])

n_list.sort(reverse = True)

number = '0'
for j in n_list:
    number = number + j

number = int(number)

if number % 30 == 0:
    print(number)
else:
    print(-1)
'''
# 푼 시간
22분

# 채점
정답

# 느낀 점
잘 풀었다.
직접 30의 배수를 써보며 규칙을 살펴보려 노력했다.
정답이라 기쁘다.
'''