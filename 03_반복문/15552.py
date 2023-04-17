"""빠른 A+B""" 

T = int(input())
list = []
for i in range(T):
    a, b = map(int, input().split())
    list.append(a+b)

for i in range(T):
    print(list[i])
