"""문자열"""

# 테스트 케이스의 개수 T
T = int(input())

# 리스트 선언
string = []
# T개 만큼 입력받아 리스트에 저장
for i in range(T):
    str = input()
    string.append(str)

# 첫 글자와 마지막 글자 연속하여 출력
for i in range(T):
    if len(string[i]) != 1:
        print('{}{}'.format(string[i][0], string[i][len(string[i]) - 1]))
    else:
        print('{}{}'.format(string[i][0], string[i][0]))