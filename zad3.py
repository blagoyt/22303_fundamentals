# num = int(input())
# matrix = []
# for i in range(num):
#     matrix.append([])
#     for j in range(num):
#         matrix[i].append(j +1 + i * num)
# print(*matrix, sep="\n")
#
# for row in matrix:
#     print(sum(row))

row_col = int(input())
matrix = []
counter = 1
for row in range(row_col):
    matrix.append([])
    for col in range(row_col):
        matrix[row].append(counter)
        counter += 1
print(*matrix, sep="\n")

for row in matrix:
    print(sum(row))