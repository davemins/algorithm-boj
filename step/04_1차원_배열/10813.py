"""공 바꾸기"""

N, M = map(int, input().split())

bag = [0 for i in range(N)]

'바구니에 그 번호에 맞는 숫자 넣기'
for n in range(1, N+1):
    bag[n-1] = n

'i와 j바구니에 들어있는 공 교환'
for m in range(M):
    i, j = map(int, input().split())
    bag[i-1], bag[j-1] = bag[j-1], bag[i -1]

for o in bag:
    print(o, end=' ')