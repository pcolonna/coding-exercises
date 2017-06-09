# Question 3.3: Stack of plates.

# We want a data structures SetOfStacks that start a new stack when the previous stack exceeds some threshold.
#
# We need to look for two things. When you call push(), is the stack already full? In that case create a new 
# stack. When we pop(), is the stack empty afterwards? In that case, erase that stack.
# 
# We will use the previous code from 3.2, but we create a list of stacks.
# At first, I thought about creating another class and when necessary create a new instance of Stack(). Seems
# overkill.

from random import randrange

class SetOfStacks():
    
    def __init__(self, height):
        self.height = height
        self.stacks = []
        
    # 
    def push(self, value):
        
        if len(self.stacks) == 0:
            self.stacks.append([])                              # If no stack in the set of stacks, append one at the end.
        if len(self.stacks[-1]) == self.height:                 # If the last stack is high enough...
            self.stacks.append([])
        self.stacks[-1].append(value)                               # The push itself.

    # pop the top of stack. 
    def pop(self):
        
        if len(self.stacks) == 0:
            return None                                         # Empty set of stack.

        value = self.stacks[-1].pop()                           # Pop top of the last stack.

        if len(self.stacks[-1]) == 0:                           # If last stack is empty, pop it.
            self.stacks.pop()

        return value
    

if __name__ == "__main__":
    
    setofstacks = SetOfStacks(8)
    for i in range(24):
        setofstacks.push(i)
        print(i)
    print("")

    for i in range(5):
        print("Popped", setofstacks.pop())