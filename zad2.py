# num = int(input())
# matrix = []
# for i in range(num):
#     matrix.append([])
#     for j in range(num):
#         matrix[i].append(j +1 + i * num)
# print(*matrix, sep="\n")
#
# flat_matrix = []
# for row in range(len(matrix)):
#     for col in range(num):
#         flat_matrix.append(matrix[row][col])
# print(flat_matrix)

from zad1 import matrix_gen

gosho = int(input())



float_matyrix = [matrix_gen(gosho)[col][row] for col in range(gosho) for row in range(gosho)]
print(float_matyrix)