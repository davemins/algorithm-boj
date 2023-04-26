"""바구니 뒤집기"""

N, M = map(int, input().split())

bag = [0 for i in range(N)]

for n in range(1, N+1):
    bag[n-1] = n

for m in range(M):
    i, j = map(int, input().split())
    '''
    만약에 1, 4면 1, 4 / 2, 3 이렇게 두번 (4-1=3)
    그리고 2, 5면 2, 5 / 3, 4 이렇게 두번 (5-2=3)
    그리고 2, 4면 2,4 이렇게 한번 (2-4=2)
    '''
    sub = j - i + 1
    repeat = sub//2
    for o in range(repeat):
        bag[i+o-1], bag[j-o-1] = bag[j-o-1], bag[i+o-1]

for p in bag:
    print(p, end=' ')