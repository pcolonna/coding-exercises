# Question 3.4: Queue via stacks.

# Implement a MyQueue class which implements a queue using two stacks
# But:  Queue -> FIFO (First-in First-out)
#       Stack -> LIFO (Last-in First-out)

# In old_stack, we store elements in the usual stack order. The oldest at the bottom.
# In new_stack, it's the reverse order. Newest at the top.

# When we queue elements, we put them in old_stack.
# When we dequeue, we want the oldest element. So after the first dequeue(), we pop
# repeatedly the elements in old_stack and put them in new_stack. Once old_stack is empty
# we have the elements in reverse order. We can pop() new_Stack to get the element we wanted.

# Now we can push elements on old_stack everytime we queue something and pop new_stack to dequeue.
# When new_stack is empty, we repeat the reversal.
 
class MyQueue():

    def __init__(self):
        self.new_stack = []
        self.old_stack = []

    def queue(self,value):
        self.old_stack.append(value)

    def dequeue(self):

        if (len(self.old_stack) == 0) and (len(self.new_stack) == 0):
            return None
        elif len(self.new_stack) == 0:
            reverse_stack(self.old_stack,self.new_stack)
        
        value = self.new_stack.pop()

        return value

def reverse_stack(stack1, stack2):
    if len(stack1) == 0:
        return None
    while len(stack1) != 0:
        stack2.append(stack1[-1])
        stack1.pop()


if __name__ == '__main__':
    test_queue = MyQueue()
    test_queue.dequeue()

    for i in range(10):
        test_queue.queue(i)
    for i in range(5):
        print(test_queue.dequeue())
    
    print("")

    for i in range(10,20):
        test_queue.queue(i)
    
    for i in range(5):
        print(test_queue.dequeue())

    print("")
    for i in range(10):
        print(test_queue.dequeue())

