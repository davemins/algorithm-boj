"""공 넣기"""

'바구니 개수 N, 공 넣는 횟수 M'
N, M = map(int, input().split())

'바구니'
bag = [0 for i in range(N)]

'i번 바구니부터 j번 바구니까지 k번이라는 공 넣기'
for m in range(M):
    i, j, k = map(int, input().split())
    for n in range(i-1, j):
        bag[n] = k

for o in bag:
    print(o, end=' ')