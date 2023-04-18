"""A+B-7"""

T = int(input())
list_sum = []

for i in range(T):
    a, b = map(int, input().split())
    list_sum.append(a+b)

for i in range(T):
    print('Case #{}: {}'.format(i+1, list_sum[i]))