'''Question: Merge Two Sorted Lists (LeetCode 21)
 Description: Merge two sorted linked lists and return it as a new sorted list. 
 The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
 '''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

first_elmenent1=ListNode(1)
first_elmenent1.next=ListNode(2)
first_elmenent1.next.next=ListNode(4)
    
first_elmenent2=ListNode(1)
first_elmenent2.next=ListNode(3)
first_elmenent2.next.next=ListNode(4) 

def sorted_merging(element1,element2):
    list=[]
    nodelist=[]
    
    variable_element1=element1
    variable_element2=element2
    while variable_element1 and variable_element2:
        list.append(variable_element1.val)
        list.append(variable_element2.val)
        variable_element1=variable_element1.next
        variable_element2=variable_element2.next

                   
    for i in sorted(list):
        merged_list=ListNode(i)
        merged_list.next=ListNode(i+1)
        nodelist.append(merged_list)
        
                    
    return nodelist
    
            
merge=sorted_merging(first_elmenent1,first_elmenent2)
for i in range(len(merge)):
    print(merge[i].val)




class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

first_element1 = ListNode(0)
first_element1.next = ListNode(5)
first_element1.next.next = ListNode(2)

first_element2 = ListNode(4)
first_element2.next = ListNode(1)
first_element2.next.next = ListNode(4)

def sorted_merging(element1, element2):
    # Create a new dummy node to serve as the head of the result list
    dummy = ListNode(0)
    current = dummy

    # Merge the two lists
    while element1 and element2:
        if element1.val < element2.val:
            current.next = element1
            element1 = element1.next
        else:
            current.next = element2
            element2 = element2.next
        current = current.next

    # Append the remaining nodes of either list
    if element1:
        current.next = element1
    elif element2:
        current.next = element2

    return dummy.next

def print_list(node):
    while node:
        print(node.val)
        node = node.next

merge = sorted_merging(first_element1, first_element2)
print_list(merge)
