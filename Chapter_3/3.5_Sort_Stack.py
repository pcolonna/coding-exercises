# Question 3.5: Sort Stack
# 
# Sort a stack such as the smallest item is on top.
# Use only one additional temporary stack.

from random import randrange

class Stack(list):
    
    def peak(self):
        return self[-1]
    def push(self, item):
        self.append(item)
    def empty(self):
        return len(self) == 0

    def sort_stack(unsorted_stack):

        sorted_stack = Stack()

        while not unsorted_stack.empty():            
            tmp = unsorted_stack.pop()
            
            while not sorted_stack.empty() and sorted_stack.peak() > tmp:
                unsorted_stack.push(sorted_stack.pop())
            
            sorted_stack.push(tmp)
            
            while not unsorted_stack.empty() and unsorted_stack.peak() >= sorted_stack.peak():
                sorted_stack.push(unsorted_stack.pop())
        
        return sorted_stack


if __name__ == '__main__':

    
    test_items = [randrange(20) for x in range(20)]
    print(test_items)
    
    S = Stack()
    
    for item in test_items:
        S.push(item)
    S = Stack.sort_stack(S)
    
    for i, item in enumerate(sorted(test_items)):
        print("item", item, S[i])