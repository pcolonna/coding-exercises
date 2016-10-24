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

	second_mat = matrix
	lines      = len(matrix)
	columns    = len(matrix[0])

	for i in range(lines):
		for j in range(columns):
			if second_mat[i][j] == 0:
				matrix = nullify_line_cols(matrix, i,j)
	return matrix

""" Set to zeros the appropriate lines and columns."""
def nullify_line_cols(matrix, line, column):
	
	# Zeros on the line.
	for i in range(len(matrix)[0]):
		matrix[line][i] = 0

	# Zeros on the columns.
	for j in range(len(matrix)):
		matrix[line][j] = 0

	return matrix


if __name__ == "__main__":
	unittest.main()
	
		





