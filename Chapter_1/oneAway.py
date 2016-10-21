# Question 5: One Away.

import unittest

# We want to know if two strings are one edit away from one another.
# Three types of edits are possibles: insert, remove or replace a character.
# 
# Let's reason about the length of the strings.
# 
# If the diff >= 2 -> we can't get one string from the other with only one edit (min 2 insertions/deletions.)
# If dif == 1      -> we can check if one insertion or remove is enough.
# If dif == 0	   -> the only possible edit is to replace a character.

def one_away(string1, string2):

	if abs(len(string1) - len(string2)) >= 2:		# absolute value so we don't have to know which string is longer.
		return False

	if abs(len(string1) - len(string2)) == 1 :
		return check_insertion(string1, string2)

	if len(string1) == len(string2) :
		return check_replace(string1, string2)

def check_insertion(string1, string2):

	already_inserted = False;
	idx_str2 = 0
	
	for i in range(len(string1)):
		if string1[i] == 

def return check_replace(string1, string2):
if __name__ == "__main__":
	unittest.main()