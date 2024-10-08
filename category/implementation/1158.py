'''
# 문제 이해
원에서 사람들이 제거되는 순서

# 발상
완전 탐색으로

# 복잡도
사람의 수를 n이라 할 때 O(n)의 시간복잡도를 가진다.

'''
N, K = map(int, input().split())
arr = [i for i in range(1, N + 1)]  # 맨 처음에 원에 앉아있는 사람들

answer = []  # 제거된 사람들을 넣을 배열
num = 0  # 제거될 사람의 인덱스 번호

for t in range(N):
    num += K - 1
    if num >= len(arr):  # 한바퀴를 돌고 그다음으로 돌아올때를 대비해 값을 나머지로 바꿈
        num = num % len(arr)

    answer.append(str(arr.pop(num)))

print("<", end="")

for i in range(len(answer) - 1):
    print(answer[i] + ",", end="")

print(answer[len(answer) - 1] + ">")
'''
# 푼 시간
30분

# 채점
오답

# 느낀 점
짜증난다.
분명히 맞출 수 있는 쉬운 문제인데 틀렸다.
그 원인은 대충 떄려 맞추려는 태도 때문이다.
손으로 쓰면서 끝까지 검증하지 않고 구현하며 테스트하면서 검증하려 했다.
그래서 시간 다 잡아먹고 틀렸다..

풀이를 깔끔하게 쓰면서 놓치는 것이 없게 하자.
'''