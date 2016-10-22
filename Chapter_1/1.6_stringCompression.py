# Question 1.6: String Compression

"""
    Basic string compression using the counts of the repeated characters.
    We assume we receive only uppercase and lowercase letters.
    If the resulting string is not smaller, we return the original.
"""
import unittest

"""
    We look at our string letter by letter.
    We keep in mind the character in the particular sequence we are looking at.
    For example at position _, current_char == a if we saw the sequence aa...a_ before.
"""

def compress_string(original_str):

    compressed_str = ""                     # Will be our compressed string.
    current_char = original_str[0]          # Initialize with first character of the input string.
    char_count = 0                          # Count the number of occurences of the character in that sequence.
    
    for char in original_str:
        
        if char == current_char:
            char_count += 1
        
        if char != current_char:

            compressed_str += current_char      # We build the compressed string buy concatenation. First the letter.
            compressed_str += str(char_count)   # Then the count.
            
            char_count   = 1                    # Re initialize the count. At one, because the new letter counts.
            current_char = char                 # New letter we look for in a sequence.
    
    
    compressed_str += current_char              # Add the last character.
    compressed_str += str(char_count)
    
    if len(compressed_str) < len(original_str):
        return compressed_str
    else:
        return original_str

""" 
    Second version.
    We move the length comparaison inside the loop. That way we don't have to 
    process the whole string if we are already longer or equal. 
    We save some time on average.
"""

def compress_string2(original_str):

    compressed_str = ""                         
    current_char = original_str[0]              
    char_count = 0                              
    
    for char in original_str:
        
        if char == current_char:
            char_count += 1
        
        if char != current_char:
            
            compressed_str += current_char
            compressed_str += str(char_count)
            
            if len(compressed_str) > len(original_str): 
                return original_str
            
            char_count   = 1
            current_char = char
        
    compressed_str += current_char
    compressed_str += str(char_count)
    
    return compressed_str

"""
    One modification to make is if a letter appears once, we should write "a" 
    instead of "a1". 
    It save some space and could change our decision to return the original 
    string instead of the compressed one.

    e.g:    aaab -> a3b
            abbb -> ab3     instead of a1b3

    a1b3 would return the original string whereas ab3 is a better solution and 
    should be returned.
"""

def compress_string3(original_str):

    compressed_str = ""                         
    current_char = original_str[0]              
    char_count = 0                              
    
    for char in original_str:
        
        if char == current_char:
            char_count += 1
        
        if char != current_char:

            compressed_str += current_char
            if char_count > 1:                              # To decide if we add the number.
                compressed_str += str(char_count)
            if len(compressed_str) >= len(original_str):    
                return original_str
            
            char_count   = 1
            current_char = char
    
    
    compressed_str += current_char
    if char_count > 1:                                      # Not very clean. Would need a rewrite.
        compressed_str += str(char_count)
    
    return compressed_str


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
            ('aabcccccaaa', 'a2b1c5a3'),
            ('abcdef', 'abcdef')
           ]

    data_3 = [
              ('aabcccccaaa', 'a2bc5a3'),
              ('abcdef', 'abcdef')
             ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = compress_string(test_string)
            self.assertEqual(actual, expected)

    def test_string_compression2(self):
        for [test_string, expected] in self.data:
            actual = compress_string2(test_string)
            self.assertEqual(actual, expected)

    def test_string_compression3(self):
        for [test_string, expected] in self.data_3:
            actual = compress_string3(test_string)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
