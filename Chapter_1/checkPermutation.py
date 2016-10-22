# checkPermutation

import unittest
import numpy as np

"""
    First version.
    In an array, add one everytime a character appears in string1, minus 1 when appears in string2.
    The index is defined by ord(char), which returns an integer. The Unicode code point of that character.
"""
def check_permutation1(string1, string2):

    if len(string1) != len(string2):
        return False                    # String of diff length can't be permutation...

    char_set = [0 for _ in range(128)]  # Array the length of the ASCII table.

    for char in string1:
        char_set[ord(char)] += 1
    for char in string2:
        char_set[ord(char)] -= 1

    # check every value in char_set
    for element in char_set:
        if element != 0:                # If not zero, the character appeared a diff number of times in one string. 
            return False

    return True

"""
    Second version with numpy.
    
    numpy.any(a) checks if any element evaluate to True.
    If permutation, every elements are zero and so evaluates to False. 
    The 'not' then give us the right value.
    Shouldn't change the time complexity
"""
def check_permutation(string1, string2):

    if len(string1) != len(string2):
        return False                    # String of diff length can't be permutation...

    char_set = [0 for _ in range(128)]  # Array the length of the ASCII table.

    for char in string1:
        char_set[ord(char)] += 1
    for char in string2:
        char_set[ord(char)] -= 1

    
    return not np.any(char_set)         
   
# Test from solutions.
# In original code, pass test_string instead of test_string[0],test_string[1].
class Test(unittest.TestCase):
    dataT = [(['abcd', 'bacd']), (['3563476', '7334566']),
             (['wef34f', 'wffe34'])]
    dataF = [(['abcd', 'd2cba']), (['2354', '1234']), (['dcw4f', 'dcw5f'])]

    def test_cp(self):
        
        # true check
        for test_string in self.dataT:
            actual = check_permutation(test_string[0],test_string[1])
            self.assertTrue(actual)
        
        # false check
        for test_string in self.dataF:
            actual = check_permutation(test_string[0],test_string[1])
            self.assertFalse(actual)


if __name__ == "__main__":

    str1 = "asa"
    str2 = "aaa"
    
    #check_permutation(str1, str2)
    unittest.main()
    