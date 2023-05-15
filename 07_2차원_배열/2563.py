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

'''

# 색종이 개수 입력
paper = int(input())

# # 좌하 꼭짓점 좌표 입력받기
coordinate = []

for i in range(paper):
    coordi = list(map(int, input().split()))
    coordinate.append(coordi)


overlapped_area = 0

# 반복문으로 겹치는 넓이 구하기
for m in range(paper):
    for n in range(m + 1, paper):
        width1 = min(coordinate[m][0], coordinate[n][0])
        width2 = max(coordinate[m][0], coordinate[n][0])
        length1 = min(coordinate[m][1], coordinate[n][1])
        length2 = max(coordinate[m][1], coordinate[n][1])
        
        if ((width1 + 10) <= width2) or ((length1 + 10) <= length2):
            continue
        else:
            overlapped_area += (width1 + 10 - width2) * (length1 + 10 - length2)

area = paper * 100 - (overlapped_area)
print(area)