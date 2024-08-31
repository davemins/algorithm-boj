"""영수증"""

X = int(input())

N = int(input())

list_a = []
list_b = []
sum = 0

for i in range(N):
    a, b = map(int, input().split())
    list_a.append(a)
    list_b.append(b)

for i in range(N):
    sum += list_a[i] * list_b[i]

if sum == X:
    print("Yes")
else:
    print("No")