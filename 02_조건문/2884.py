"""입력값의 45분 전 시간 출력하기"""

h, m = map(int, input().split())

if h == 0:
    if m >= 45:
        m = m - 45
        print('{} {}'.format(h, m))
    else:
        h = 23
        m = m - 45 + 60
        print('{} {}'.format(h, m))
else:
    if m >= 45:
        m = m - 45
        print('{} {}'.format(h, m))
    else:
        h = h - 1
        m = m - 45 + 60
        print('{} {}'.format(h, m))