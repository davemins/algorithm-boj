"""상수"""

num = list(map(int, input().split()))

new_num1 = new_num2 = 0

new_num = [new_num1, new_num2]

for i in range(len(num)):
    number = num[i]
    for j in range(3):
        new_num[i] += (number % 10) * (10 ** (2-j))
        number = number // 10

print(max(new_num))