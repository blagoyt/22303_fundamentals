# N = int(input())
# matrix = []
#
# for _ in range(N):
#     row = list(map(int, input().split(", ")))
#     matrix.append(row)
#
# diagonal_sum = sum(matrix[i][i] for i in range(N))
#
# print(f"{diagonal_sum}")

row_col = int(input())
matrix = []
counter = 1
for row in range(row_col):
    matrix.append([])
    for col in range(row_col):
        matrix[row].append(counter)
        counter += 1
print(*matrix, sep="\n")

primary_diagonal_sum = 0
for r in range(row_col):
    primary_diagonal_sum += matrix[r][r]