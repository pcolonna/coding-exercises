
#	Question 1: isUnique

import unittest
import random
import string

# First solution. Very Basic.
# Compare every letter with every other letter.
# 
# Time complexity O(n^2).

def isUnique(yourString):
	
	if len(yourString) > 128:
		return False

	else:
		for i in range(len(yourString)):
			for j in range(len(yourString)):
				if i != j and yourString[i] == yourString[j]:
					return False
		return True



# Solution from book
# Create an array of boolean the size of the ASCII table.
# Initialize at False. When a character i is found put the element i at True.
# If you see it again, it's already at True and you know it's not unique. 
# 
# Time complexity O(n).

def isUnique2(string):
	# Assuming character set is ASCII (128 characters)
	if len(string) > 128:
		return False

	char_set = [False for _ in range(128)]						# Fill an array of boolean, set to False. For now, no character has been encountered.
	for char in string:
		val = ord(char)											# ord() expected string of length 1. Returm a number e.g ord("a") = 97, ord("3") = 51
		if char_set[val]:										# used as index in the char_set
			# Char already found in string
			return False
		char_set[val] = True

	return True


# Class testing our 2 functions.
# From github book solutions + some added tests.
class Test(unittest.TestCase):
	
	dataT = [('abcd'), ('s4fad'), ('')]
	dataF = [('23ds2'), ('hb 627jh=j ()')]

	# Random string longer than the number of ASCII character. 
	rdm_string = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(129))
	print(rdm_string)

	def test_unique(self):
		
		# true check
		for test_string in self.dataT:
			actual  = isUnique(test_string)
			actual2 = isUnique2(test_string)
			self.assertTrue(actual)
			self.assertTrue(actual2)
		
		# false check
		for test_string in self.dataF:
			actual = isUnique(test_string)
			actual2 = isUnique2(test_string)
			self.assertFalse(actual)
			self.assertFalse(actual2)

		# Length check.
		actual  = isUnique(rdm_string)
		actual2 = isUnique2(rdm_string)
		self.assertFalse(actual)
		self.assertFalse(actual2)

			



if __name__ == "__main__":
	
	#isUnique('abc')
	
	rdm_string = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(12))
	print(rdm_string)
	
	unittest.main()

	# Anything after unittest is not executed. 
	#rdm_string = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(12))
	#print(rdm_string)
	
