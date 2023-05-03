"""숫자의 합"""

amount = input()

number = int(input())

number_list = []

while(number!=0):
    number_list.append(number%10)
    number = number//10

sum = 0

for n in number_list:
    sum += n

print(sum)