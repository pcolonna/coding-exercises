# Question 3.2: Stack Min.
# 
#   Design stack which has a function min which returns the min element in O(1)

class StackMin():
    
    def __init__(self):
        self.stack   = []
        self.minimun = []

    # standard push, which put value on top of stack.
    # + update minimum if necessary.
    def push(self, value):
        
        self.stack.append(value)                                # The push itself.

        if len(sel.minimum) == 0 or value <= self.min[-1]:      # If list empty or if the value is inferior to current min,
            self.min.append(value)                              # append new min. Can have multiple equals minimums.

    # pop the top of stack. Update minimum if necessary.
    def pop(self):
        
        if len(self.stack) == 0:
            return None                                         # Empty stack.

        value = self.stack.pop()                                # Pop top of the stack. Built-in function.

        if value == self.min[-1]:                               # If value equals min, we pop the end of the list. Update mins.                         
            self.min.pop()                                      # 

        return value
        