"""배수와 약수"""

while (1):
    first_number, second_number = map(int, input().split())
    if first_number == 0 and second_number == 0:
        break
    if (first_number < second_number and second_number % first_number == 0):
        print("factor")
    elif (first_number > second_number and first_number % second_number == 0):
        print("multiple")
    else:
        print("neither")