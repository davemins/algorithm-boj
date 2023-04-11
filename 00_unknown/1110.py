N = int(input())
count = 0

number = N
while True:

    b = number//10 + number%10
    number = (number%10)*10 + b%10
    count += 1

    if number == N:
        print(count)
        break