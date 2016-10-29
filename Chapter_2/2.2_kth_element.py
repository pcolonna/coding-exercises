# Question 2.1: Return Kth to last.

"""
	Implement an algorithm to find the kth to last element of a singly linked list.
	I define k such as k = 1 is the last element. (k=0 is also acceptable.)
	At first, i chose k=0. But k = 1 gives consistent results between the two methods.
"""
from collections import deque
from random import randint

"""
	We will use deque, double-ended queue. According to the doc, they are implemented 
	as a doubly-linked list. At first I wanted to only use operations available to single 
	linked list, but it seems deque don't have a .next method.
 	We pop the k-1 last element. The next pop is the intended value.
"""
def find_kth(your_list, k):

	for i in range(k-1):						# Pop in range(k-1) if you want k = 1 as last element. range(k) otherwise.
		your_list.pop()

	return your_list.pop()


		

if __name__ == "__main__":

	min_val = 0
	max_val = 99
	max_len = 10
	test_k  = 4

	test_list = deque()
	test_list = [randint(min_val, max_val) for i in range(max_len)]
	test_list2 = [randint(min_val, max_val) for i in range(max_len)]
	
	print(test_list)
	print(test_list2)
	
	kth = find_kth(test_list, test_k)
	
	
	print(kth)
	
	