# Question 1.9: String rotation

"""
We have two strings, s1 and s2. We want to know if s2 is a rotation of s1 using only one call to 
is_substring.

is_substring checks if one word is a substring of another.
"""

import unittest

""" From solution """
def is_substring(string, sub):
    return string.find(sub) != -1

def string_rotation(s1, s2):
    if len(s1) == len(s2) != 0:
        return is_substring(s1 + s1, s2)
    return False

"""
	Here we implement the function is_subtring in the case where the python
	function string.find() didn't exist.

	Do so we check the first letter of the string with the first of the substring.
	If equal, we move to look at the next element on both string.
	If different, we keep the same position on the string but start over on the substring. 
	To do so, we reset index to 0.

"""
def is_substring_manual(string, sub):

	i = 0
	index 		= 0
	isSubstring = False
	
	while i < len(string) - 1:
		
		if index == len(sub)-1:
			return True

		elif string[i] == sub[index]: 
			i += 1
			index += 1
			isSubstring = True
		
		elif string[i] != sub[0]:
			index = 1
			i += 1
			isSubstring = False
		
		elif string[i] == sub[0]:
			i += 1
			index = 1
			isSubstring = True
		
	return isSubstring

def string_rotation2(s1, s2):
    if len(s1) == len(s2) != 0:
        return is_substring_manual(s1 + s1, s2)
    return False

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [ ('fox', 'ox', False),
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False),
        ('foo', 'fxxx', False)
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.data:
            actual = string_rotation2(s1, s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()