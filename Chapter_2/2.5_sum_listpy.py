# Question 2.5 Sum lists


from LinkedList import LinkedList

# We add the number node by nodes.
# If necessary, we carry the 1 to the next node.
def sum_list(ll_1, ll_2):
    result         = 0 
    carry          = 0
    head_1, head_2 = ll_1.head, ll_2.head
    result_ll      = LinkedList()

    while head_1 or head_2:
        result = carry
        if head_1:
            result += head_1.value  
            head_1 = head_1.next

        if head_2:
            result += head_2.value
            head_2  = head_2.next

        result_ll.add(result % 10)   # Add the first digit.
        carry = result // 10         # // only gives the the integer part, therefore the carry

    if carry:
        result_ll.add(carry)         # Once we walked through all the nodes, if a carry remains
                                     # we add it to the list

    return result_ll
        
# Digits are stroed forward.
# If one list is shorter than the other, we pad the shoter one.
def sum_list_forward(ll_1, ll_2):

    #Check size and pad the shorter list.
    if len(ll_1) < len(ll_2):
        for i in range(len(ll_2) - len(ll_1)):
            ll_1.add_to_beginning(0)
            #ll_1.add(0)
    else:
        for i in range(len(ll_1) - len(ll_2)):
            ll_2.add_to_beginning(0)
            #ll_2.add(0)

    print("Padded Lists : ")
    print(ll_1)
    print(ll_2)

    result         = 0 
    head_1, head_2 = ll_1.head, ll_2.head
    print("head_1 ", head_1.value)
    #Iterate through the list
    while head_1 and head_2:
        result = (result*10) + head_1.value + head_2.value  # result*10 shifts the previous value. 
        head_1 = head_1.next                              # next node, next value to add.
        head_2 = head_2.next

    print(result)
    # Create new linked list
    ll = LinkedList()
    ll.add_multiple([int(i) for i in str(result)])

    return ll



if __name__ == "__main__":

    ll_a = LinkedList()
    ll_a.generate(4, 0, 9)
    ll_b = LinkedList()
    ll_b.generate(3, 0, 9)
    print(ll_a)
    print(ll_b)
    print(sum_list(ll_a, ll_b))
    print(sum_list_forward(ll_a, ll_b))