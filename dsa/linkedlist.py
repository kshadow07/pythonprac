## LEETCODE 206


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
head1=Node(1)
head2=head1.next=Node(2)
head3=head2.next=Node(3)
head4=head3.next=Node(4)
head5=head4.next=Node(5)

class Solution:
    def reverseList(self,head1):
        prev=None
        current=head1
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        return prev
        
solution = Solution()
reversed_head = solution.reverseList(head1)

while reversed_head:
    print(reversed_head.value)
    reversed_head = reversed_head.next               