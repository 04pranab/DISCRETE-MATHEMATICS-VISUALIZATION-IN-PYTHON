def relation_matrix(A, R):
    n = len(A)
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if (A[i], A[j]) in R:
                matrix[i][j] = 1

    return matrix

A = [1, 2, 3, 4]
R = [(1, 2), (2, 3), (3, 4), (4, 1), (1, 4)]

matrix_R = relation_matrix(A, R)
for row in matrix_R:
    print(row)