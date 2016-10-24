# Question 1.7: Rotate Matrix

#Solution from book...

import unittest

""" Solution from the book go from the outer layer towards the center. """
def rotate_matrix(matrix):
    '''rotates a matrix 90 degrees clockwise'''
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        for i in range(first, last):
            # save top
            top = matrix[layer][i]
            print(top)
            # left -> top
            matrix[layer][i] = matrix[-i - 1][layer]

            # bottom -> left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]

            # top -> right
            matrix[i][- layer - 1] = top
    return matrix

""" 
    Here we go inside out.
    We rotate the center/inner layer first and make our way toward the top layers.
"""
def rotate_matrix_inside_out(matrix):
    '''rotates a matrix 90 degrees clockwise'''
    n = len(matrix)
    
    for layer in range(n // 2, -1, -1):
        first, last = layer, n - layer - 1
        for i in range(first, last):
            # save top
            top = matrix[layer][i]
            print("top " + str(top))
            # left -> top
            matrix[layer][i] = matrix[-i - 1][layer]

            # bottom -> left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]

            # top -> right
            matrix[i][- layer - 1] = top

    print(matrix)
    return matrix

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])
    ]
    
    data2 = [                                       # Quick dirty fix.
        ([                                          # The two tests were passing separately but not one after the other.
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])
    ]
    
    def test_rotate_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = rotate_matrix(test_matrix)
            self.assertEqual(actual, expected)
    
    def test_rotate_matrix_inside_out(self):
        for [test_matrix, expected] in self.data2:
            actual = rotate_matrix_inside_out(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
