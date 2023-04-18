"""A+B-5"""
list_sum = []
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    list_sum.append(a+b)

for i in range(len(list_sum)):
    print(list_sum[i])