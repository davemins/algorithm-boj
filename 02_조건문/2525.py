"""오븐 시계"""

h, m = map(int, input().split())
time = int(input())

time_h = time // 60 + h # 더한 시간
time_m = time % 60 + m # 더한 분

time_h_h = time_h + time_m // 60
time_m_m = time_m % 60

''''time_h_h가 24 이상이면 24를 빼준다'''

if time_h_h >= 24:
    time_h_h = time_h_h - 24
    print('{} {}'.format(time_h_h, time_m_m))
else:
    print('{} {}'.format(time_h_h, time_m_m))