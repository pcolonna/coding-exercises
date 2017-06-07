# Question 3.2: Stack Min.
# 
#   Design stack which has a function min which returns the min element in O(1)

from random import randrange

class StackMin():
    
    def __init__(self):
        self.stack   = []
        self.minimum = []

    # standard push, which put value on top of stack.
    # + update minimum if necessary.
    def push(self, value):
        
        self.stack.append(value)                                 # The push itself.

        if len(self.minimum) == 0 or value <= self.minimum[-1]:  # If list empty or if the value is inferior to current min,
            self.minimum.append(value)                           # append new min. Can have multiple equals minimums.

    # pop the top of stack. Update minimum if necessary.
    def pop(self):
        
        if len(self.stack) == 0:
            return None                                         # Empty stack.

        value = self.stack.pop()                                # Pop top of the stack. Built-in function.

        if value == self.minimum[-1]:                           # If value equals min, we pop the end of the list. Update mins.                         
            self.minimum.pop()                                   

        return value
    
    def get_min(self):
        if len(self.minimum) == 0:
            return None;
        return self.minimum[-1]


if __name__ == "__main__":
    
    S1 = StackMin()
    S2 = StackMin()
    test_list = [randrange(100) for x in range(10)]
    S2.push(42)
    for num in test_list:
        S1.push(num)
        S2.push(num)
        print(num) 
    print("")
    for i in range(len(test_list)):
        print("new pop", S1.pop(), S2.pop())
        print("new min", S1.get_min(), S2.get_min())

