def matrix_gen(number):
    matrix = []
    counter = 1
    for row in range(number):
        matrix.append([])
        for col in range(number):
            matrix[row].append(counter)
            counter += 1
    return matrix

row_col = int(input())
print(*matrix_gen(row_col), sep="\n")

#
# num = int(input())
# matr = []
# for i in range(num):
#     matr.append([])
#     for j in range(num):
#         matr[i].append(j +1 + i * num)
# print(*matr, sep="\n")