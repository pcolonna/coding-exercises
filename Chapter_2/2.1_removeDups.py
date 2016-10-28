# Question 2.1: Remove Dups.

""" Remove duplicates from an unsorted linked list. """

import unittest

"""
	We go through the list element by element. 
	If the element is not already in our cleaned up list, we append it to it.
	Otherwise, we move on.

	"if element in clean_list" return directly True or False depending on if the 
	element actually belongs to the list. 
	The "not" is there to denotes the absence of a specific element, meaning we met it 
	for the first time. Therefore we append.
"""

def find_duplicates(your_list):

	clean_list = []

	for element in your_list:
		if not(element in clean_list):
			clean_list.append(element)

	return clean_list

"""
	Concerning the time complexity.

	Iterating through the list is O(N).
	Append is apparently implemented in O(1).
	The "x in s" is sequential and therefore in O(N).

	So every time we test and search for an element, we go through the list
	until we either find the element or run out of list. We don't exactly do N operations
	each times, we can approximate it that way. 

	So this method would in O(NxN) = O(N^2).
"""

"""
	A better way would be to use a dictionary. In python, dict are implemented as hash tables.
	And with hash tables, search/access can be done in O(1) on average.

	It would reduce complexity to O(1).
"""
if __name__ == "__main__":
	unittest.main()