"""그대로 출력하기"""

while True:
    try:
        string = input()
        print(string)
    except EOFError:
        break