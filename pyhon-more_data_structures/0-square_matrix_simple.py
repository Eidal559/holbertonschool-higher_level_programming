#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[x * x for x in row] for row in matrix]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        result_matrix[i][j] = matrix[i][j] ** 2
        
        return result_matrix
    
    input_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    result = square_matrix_simple(input_matrix)
    print(result)
