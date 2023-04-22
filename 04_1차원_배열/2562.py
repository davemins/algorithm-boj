"""최댓값"""

ls = []

for i in range(9):
    a = int(input())
    ls.append(a)

b = max(ls)
print(b)

for i in range(9):
    if ls[i] == b:
        c = i + 1
        break
print(c)