# Question 3.6: Animal Shelter.
# 
# People must adopt animal. Either choose a dog, a cat, or the oldest of both.
# Must implement the data structure to perform enqueue(), dequeue_dog(), dequeue_cat()
# and dequeue_any().

# "Deques are a generalization od stacks and queues" that perform "appends and pops from either
# side of the deque with approximately the same O(1) performance in either direction." according
# to the python doc. 
from collections import deque 			

class Shelter():

	def __init__(self):
		self.cat_queue       = deque()			# We use seperate stack for each animal type.
		self.dog_queue 		 = deque()
		self.time_of_arrival = 0				# Use to determined the oldest animal overall.

	def enqueue(self, animal, name):
		
		if animal == "cat"
			self.dog_queue.appendleft(name, self.time_of_arrival)
			self.time_of_arrival += 1
			
		elif animal == "dog":
			self.dog_queue.appendleft(name, self.time_of_arrival)
			self.time_of_arrival += 1

		
