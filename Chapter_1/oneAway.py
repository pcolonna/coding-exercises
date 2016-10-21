# Question 5: One Away.

import unittest

# We want to know if two strings are one edit away from one another.
# Three types of edits are possibles: insert, remove or replace a character.
# 
# Let's reason about the length of the strings.
# 
# If the diff >= 2 -> we can't get one string from the other with only one edit (min 2 insertions/deletions.)
# If dif == 1      -> we can check if one insertion or remove is enough.
# If dif == 0      -> the only possible edit is to replace a character.

def one_away(string1, string2):

    if abs(len(string1) - len(string2)) >= 2:       # absolute value so we don't have to know which string is longer.
        return False

    if abs(len(string1) - len(string2)) == 1 :
        return check_insertion(string1, string2)

    if len(string1) == len(string2) :
        return check_replace(string1, string2)


# Here we performs the operations to check if only one insertion is necessary.
# 
# We compare character by character. 
# 
# If they're equals, great. Otherwise we check the variable already_inserted 
# to see if already performs the edit.
# 
# If already_inserted == True,  another edit is therefore necessay and we fail.
# If already_inserted == False, we set it to True and change the index of the 
# character we look at in the other string.
# 
# example: aba    string 1
#          ba     string 2
#          
#          -> we look first at string1[0] and string2[0]. 
#          -> then we look at string1[1] but at string2[0] again.
# 
# I chose to look at the longer first. So we need to check the length first.

def check_insertion(string1, string2):

    already_inserted = False;
    i_short_str = 0

    long_str  = string1 if len(string1) > len(string2) else string2         # Conditional assignement, depending on the length of each string.
    short_str = string1 if len(string1) < len(string2) else string2         # Probaly better than if...else, but could be improved.

    for i in range(len(string1)):
        
        if long_str[i] != short_str[i_short_str] and already_inserted:      
            return False
        
        if long_str[i] != short_str[i_short_str] and not already_inserted:
            already_inserted = True

            #   Following line actually useless. Wrong even...
            #i_short_str = max(0, i_short_str - 1)                          # We shift the index we look at in the shorter string. Make sure we 
                                                                            # don't go into the negative if we insert from the beginning.
        else:
            i_short_str += 1                                                # If equals, we increment and keep going.

    return True

# If the same length, we check how many replacement we need to make.
# We just compare character by character.

def check_replace(string1, string2):

    already_replaced = False;
    i_short_str = 0
    
    for i in range(len(string1)):
        if long_str[i] != short_str[i_short_str] and already_inserted:      # More than one edit.
            return False
        
        if long_str[i] != short_str[i_short_str] and not already_inserted:
            already_inserted = True
            
    return True


def return check_replace(string1, string2):
if __name__ == "__main__":
    unittest.main()