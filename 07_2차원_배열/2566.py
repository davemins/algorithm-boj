"""최댓값"""

# matrix = [list(map(int, input().split())) for _ in range(9)]

# for row in matrix:
#     print(' '.join(map(str, row)))

# max_list = []

# for i in matrix:
#     max_list.append(max(i))

# print(max(max_list))

# max_row = max_list.index(max(max_list))
# max_column = matrix[max_row].index(max(matrix[max_row]))

# print(max_row + 1, max_column + 1)

matrix = [list(map(int, input().split())) for _ in range(9)]

max_value = max(map(max, matrix))
print(max_value)

for i in range(9):
    for j in range(9):
        if matrix[i][j] == max_value:
            print(i + 1, j + 1)
            break