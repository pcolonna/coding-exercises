# Question 2.3: delete_middle_node.

"""
    Algo to delete a node in the middle of a singly linked list.
    Not necessarily the middle, just any node that is not the first or last one.
"""

from LinkedList import LinkedList

"""
    To delete a node in a linked list, you can just skip it. Jump or ignore it.
    So if you want to delete node n, change its value to the value of node n+1 ,
    and change the ref from n to n+2. We just shift everythong.

    1 -> 2 -> 3 -> 4 -> 5 -> 7 -> 8 -> 9
                   copy | 
                        v   
    1 -> 2 -> 3 -> 4 -> 7 -> 7 -> 8 -> 9
     
    then skip 

    1 -> 2 -> 3 -> 4 -> 7 -> 8 -> 9
"""
def delete_mid_node(node):

    node.value = node.next.value            # Change/copy value from the next node.
    node.next  = node.next.next             # Point two nodes ahead, which delete a node in practice.

"""
    We should also deal with the case where the node is the last one in the list. 
    Our algo doesn't work in that situation yet.
    
"""

if __name__ == "__main__":

    ll = LinkedList()
    ll.add_multiple([1, 2, 3, 4])
    middle_node = ll.add(5)
    ll.add_multiple([7, 8, 9])
    
    print(ll)
    delete_mid_node(middle_node)
    print(ll)