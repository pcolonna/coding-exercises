# Question 3: Palindrome Permutation

# Our palindrome permutation can have either an even number of occurences for each character
# or one odd and all the rest even.
# 
# We count the occurences in char_set.
# Then we check if the parity of each element.
# 
# odd_nb_char tells us if a character alrerady appeared an odd number of times, and allows us
# to stop early if necessary.


import unittest


# This version is case sensitive. Very case sensitive.
# By that I mean that all characters are counted separately, even spaces.
# So "aa" is true but not "aA".
# Also "aAa" is true but not "aA a", and "aA  a" (two spaces) is a palindrome again.
# 
# We need to make some changes if we want to have the usually expected behavior, 
# case insensitive and oblivious to spaces.

def palindrome_sensitive(yourString):

	odd_nb_char = False;					# Is set to True if a character appears an odd number of times.
	char_set 	= [0 for _ in range(128)]	# Will be used to count the number of times a character is in the string. 
											# Array the lenght of the ascii table. 
	
	for char in yourString:
		char_set[ord(char)] += 1;			# ord(char) gives us the index in the array. Increment by one each time a character is found.

	for element in char_set:				# Iterate through your set of characters.
		if element % 2 != 0:				# Check if it's an odd number. 
			if odd_nb_char == True:			# If it's not the first time a character appears an odd number of times,
				return False				# the string can't be a palindrome.
			else:
				odd_nb_char = True			# Otherwise update odd_nb_char

	return True	



# Here we deal with the spaces.
# A quick way to ignore them is to reset the element in char_set corresponding to SPACE
# to zero.

def palindrome_no_spaces(yourString):

	idx_space   = ord(" ")					# ASCII code point of SPACE. Index of element we want to reset.
	odd_nb_char = False;					
	char_set 	= [0 for _ in range(128)]		
											 
	
	for char in yourString:
		char_set[ord(char)] += 1;			

	#char_set[32]       = 0					# 32 is the ASCII code point of SPACE.
	#char_set[ord(" ")] = 0					# Or you can use ord() again instead of a random number appearing out of nowhere.
	char_set[idx_space] = 0					# Using a variable may even be better.

	for element in char_set:				
		if element % 2 != 0:				
			if odd_nb_char == True:			
				return False				
			else:
				odd_nb_char = True			

	return True			



# We assume here we are only interested to "normal" palindromes.
# Meaning we only receive letters, it's case insensitive and spaces don't matter.
# 
# One solution is just to lowercase every character before counting/updating char_set.

def palindrome_alphabet(yourString):

	idx_space   = ord(" ")					# ASCII code point of SPACE. Index of element we want to reset.
	odd_nb_char = False;					
	char_set 	= [0 for _ in range(128)]		
											 
	
	for char in yourString:
		lower_char = lowercase(char)
		char_set[ord(lower_char)] += 1;			

	char_set[idx_space] = 0					# Using a variable may even be better.

	for element in char_set:				
		if element % 2 != 0:				
			if odd_nb_char == True:			
				return False				
			else:
				odd_nb_char = True			

	return True								



class Test(unittest.TestCase):
    '''Test Cases'''
    data = [('a a', True)]
        #('Tact Coa', True)]#,
        #('jhsabckuj ahjsbckj', True),
        #('Able was I ere I saw Elba', True),
        #('So patient a nurse to nurse a patient so', False),
        #('Random Words', False),
        #('Not a Palindrome', False),
        #('no x in nixon', True),
        #('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = palindrome_sensitive(test_string)
            self.assertEqual(actual, expected)


if  __name__ == "__main__":
	unittest.main()