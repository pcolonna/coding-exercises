#Question 2.4: Partition

"""
	Partition a linked list around a value x.

	To do so, we create a new list. 
	Elements bigger than the pivot are added to the tail, those smaller to the head.
	We don't care about ordering inside a partition.
"""

from LinkedList import LinkedList

def partition(list, pivot):

	partitioned_list = LinkedList()
	node = list.head

	while(node != None):
		if (node.value < pivot):
			partitioned_list.add_to_beginning(node.value)
		else:
			partitioned_list.add(node.value)
		node = node.next

	return partitioned_list

if __name__ == "__main__":

	test_list = LinkedList()
	test_list.add_multiple([3,5,8,5,10,2,1])	#linked list from example.

	print(test_list)
	print(partition(test_list, 5))

	