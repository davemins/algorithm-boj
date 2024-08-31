"""색종이"""

'''

[[a, b], [a+10, b], [a, b+10], [a+10, b+10]]

n번째 색종이가 다른 색종이와 겹치는 넓이를 구하는 함수를 만들어버리자


3 7
15 7
5 2

a1 b1
a2 b2
a3 b3

-> a1 +10 <= a2이면 끝내기, a1 + 10 > a2이면 

100 * 100 이차원 리스트에서 차지하는 부분은 1로 바꾸어주어 넓이 구한다

'''

N = int(input())

paper = [[0 for i in range(100)] for j in range(100)]

for i in range(N):
    col, row = map(int, input().split())
    for j in range(col, col + 10):
        for k in range(row, row + 10):
            paper[j - 1][k - 1] = 1

area = 0
for l in paper:
    area += sum(l)

print(area)