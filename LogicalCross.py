def logical_multiply(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Matrices dimensions are not compatible for multiplication.")

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            value = 0
            for k in range(len(matrix2)):
                value |= (matrix1[i][k] & matrix2[k][j])  # Logical OR for multiplication
            row.append(value)
        result.append(row)

    return result

matrix1 = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 1, 1]
]

matrix2 = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 1]
]

result_matrix = logical_multiply(matrix1, matrix2)
print("Result after Logical Multiplication: ")
for row in result_matrix:
    print(row)