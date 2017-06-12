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
		
		if animal == "cat":
			self.dog_queue.append((name, self.time_of_arrival))			# We consider left to be the beginning of the queue.
			self.time_of_arrival += 1
			
		elif animal == "dog":
			  self.dog_queue.append((name, self.time_of_arrival))		# Append() appends to the right. 
			  self.time_of_arrival += 1

		else:
			print("Invalid type. Retry.")

	def dequeue_cat(self):
		if not len(self.cat_queue) == 0:
			return self.cat_queue.pop()[0]								# We only return the name.

	def dequeue_dog(self):
		if not len(self.dog_queue) == 0:
			return self.dog_queue.pop()[0]								 

	def dequeue_any(self):
		
		# We first need to find the oldest animal.
		oldest_dog = self.dog_queue[0] if not len(self.dog_queue) == 0 else (None, -1)	# Deque allows fast access on both end. Otherwise we would
		oldest_cat = self.cat_queue[0] if not len(self.cat_queue) == 0 else (None, -1)	# to pop() the oldest of queue, compare, and then re-append.

		if oldest_cat[1] == -1 and oldest_dog[1] == -1:
			return None
			
		if 	 oldest_cat[1] >= oldest_dog[1]:	
				return oldest_cat

		elif oldest_dog[1] >  oldest_cat[1]:
				return oldest_dog




if __name__ == '__main__':
	
	Q = Shelter()

	from random import randrange
	test_list = [randrange(7) for x in range(20)]
	for i, x in enumerate(test_list):
		if x < 4:
			if i%2: 
				animal_type = "cat" 
			else: 
				animal_type = "dog"
			test_list[i] = ("enqueue", Q.enqueue, animal_type, animal_type + "#" + str(i))
		elif x == 4:
			test_list[i] = ("dequeue any", Q.dequeue_any)
		elif x == 5:
			test_list[i] = ("dequeue cat", Q.dequeue_cat)
		elif x == 6:
			test_list[i] = ("dequeue dog", Q.dequeue_dog)


	for operation in test_list:
		if len(operation) == 4:
			print(operation[0], operation[2], operation[3])
		else:
			print(operation[0])
			print(operation[1])	
	