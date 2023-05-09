"""행렬 덧셈"""

# row, column = map(int, input().split())

# matrix_1 = [[] for i in range(row)]
# matrix_2 = [[] for i in range(row)]

# for i in range(column):
#     row_series = input()
#     row_series = list(row_series.split())
#     matrix_1[i] = row_series

# for j in range(column):    
#     row_series = input()
#     row_series = list(row_series.split())
#     matrix_2[j] = row_series

# matrix_sum = [[] for i in range(row)]

# for m in range(column):
#     for n in range(row):
#         matrix_sum[m].append(int(matrix_1[m][n]) + int(matrix_2[m][n]))

# for row in matrix_sum:
#     print(' '.join(map(str, row)))

row, column = map(int, input().split())

matrix_1 = [list(map(int, input().split())) for _ in range(row)]
matrix_2 = [list(map(int, input().split())) for _ in range(row)]

matrix_sum = [[matrix_1[i][j] + matrix_2[i][j] for j in range(column)] for i in range(row)]

for row in matrix_sum:
    print(' '.join(map(str, row)))
