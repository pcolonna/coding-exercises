# Question 3.4: Queue via stacks.

# Implement a MyQueue class which implements a queue using two stacks
# But:  Queue -> FIFO (First-in First-out)
# 		Stack -> LIFO (Last-in First-out)

# In old_stack, we store elements in the usual stack order. The oldest at the bottom.
# In new_Stack, it's the reverse order. Newest at the top.

# When we queue elements, we put them in old_stack.
# When we dequeue, we want the oldest element. So after the first dequeue(), we pop
# repeatedly the elements in old_stack and put them in new_stack. Once old_stack is empty
# we have the elements in reverse order. We can pop() new_Stack to get the element we wanted.

# Now we can push elements on old_Stack everytime we queue something and pop new_stack to dequeue.
# When new_stack is empty, we repeat the reversal.
 
class MyQueue():

	def __init__(self):
		self.new_stack = []
		self.old_stack = []


