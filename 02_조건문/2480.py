"""주사위 세개"""

dice = list(map(int, input().split()))
box = []
n = 1

for i in dice:
    if i in box:
        n = n + 1
        s = i
    else:
        box.append(i)

if n == 3:
    print(10000+s*1000)
elif n == 2:
    print(1000+s*100)
elif n == 1:
    print(max(dice)*100)