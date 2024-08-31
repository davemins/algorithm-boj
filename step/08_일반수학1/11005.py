"""진법 변환2"""

number, base = map(int, input().split())

digits = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
            "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
            "U", "V", "W", "X", "Y", "Z")
def solution(n, b):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, b)
        rev_base += digits[mod]

    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력
    return rev_base[::-1] 
    
print(solution(number, base))