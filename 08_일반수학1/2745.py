"""진법 변환"""

number, base = map(str, input().split())
base = int(base)

print(int(number, base))