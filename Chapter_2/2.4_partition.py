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

# In this case, we do not create another list.
def partition_in_place(list, pivot):

    current_node = list.tail = list.head        # Need to go back on that line.

    while current_node:
        
        next_node         = current_node.next                    
        current_node.next = None

        if current_node.value < pivot:
            current_node.next = list.head
            list.head         = current_node
        else:
            list.tail.next = current_node 
            list.tail      = current_node

        current_node = next_node

    

if __name__ == "__main__":

    test_list = LinkedList()
    test_list.add_multiple([3,5,8,5,10,2,1])    #linked list from example.

    """print(test_list)
    print(partition(test_list, 5))
    print(partition_in_place(test_list, 5))
    print(test_list)
"""
    ll = LinkedList()
    ll.generate(10, 0, 99)
    print(ll)
    partition_in_place(ll, 50) #ll.head.value)
    print(ll)
    print(ll.__len__())
    