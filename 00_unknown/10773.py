"""제로"""

k = int(input())

money = []
for i in range(k):
    m = int(input())
    if m == 0:
        money.pop()
    else:
        money.append(m)

print(sum(money))