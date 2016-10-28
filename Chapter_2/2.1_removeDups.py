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

if __name__ == "__main__":
	unittest.main()