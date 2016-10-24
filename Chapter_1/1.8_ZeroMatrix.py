""" Question 1.8: Zero Matrix.

    We have a MxM matrix. 
    If we found an element == 0, we set row and columns to zeros.

    We will have to deal with inserted 0s vs original 0s.
    Otherwise, the matrix is gonna end up full of zeros...
"""

import unittest


"""
    First solution.

    We keep second matrix identical to the original matrix.
    When we encounter a zero we only change one or the other.

    Not an optimal solution. The space is in O(MN) (or O(M^2) if square matrix).
    Plus copying the matrix is expensive, O(MN).
"""

def zero_matrix_with_copy(matrix):

    # At first i use second_mat = matrix[:], but the inner object kept their references
    # and i ended up with a matrix of zeros. 
    second_mat = [[matrix[x][y] for y in range(len(matrix[0]))] for x in range(len(matrix))] # Correct copy by value.
    lines      = len(matrix)
    columns    = len(matrix[0])

    for i in range(lines):
        for j in range(columns):
            if second_mat[i][j] == 0:
                matrix = nullify_line_cols(matrix, i,j)
               
    print(matrix)
    return matrix

""" Set to zeros the appropriate lines and columns."""
def nullify_line_cols(mat, line, column):
    
    # Zeros on the line.
    for i in range(len(mat[0])):
        mat[line][i] = 0

    # Zeros on the columns.
    for j in range(len(mat)):
        mat[j][column] = 0
    #print(matrix)
    return mat




class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix_with_copy(test_matrix)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
    
        





