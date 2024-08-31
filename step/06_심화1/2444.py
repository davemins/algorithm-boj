"""별 찍기 - 7"""

mount = int(input())

for i in range(mount):
    print(" " * (mount - i), "*" * (2 * i - 1))

for i in range(mount, 0, -1):
    print(" " * (mount - i), "*" * (2 * i - 1))