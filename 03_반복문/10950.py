"""A+B-3"""

T = int(input())

list = []

for i in range(T):
    a, b = map(int, input().split())
    list.append(a+b)

for i in range(T):
    print(list[i])