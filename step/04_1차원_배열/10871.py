"""X보다 작은 수"""

N, X = map(int, input().split())

A = list(map(int, input().split()))

B = []
for i in A:
    if i < X:
        B.append(i)

for j in B:
    print(j, end=' ')