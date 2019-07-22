# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        if l1 == None: return l2
        if l2 == None: return l1
        
        carry_over = 0
        first_node = ListNode(0)
        pointer = first_node
        
        while l1 and l2:
            pointer.next = ListNode((l1.val+l2.val+carry_over)%10)
            carry_over = (l1.val + l2.val + carry_over)//10
            l1 = l1.next
            l2 = l2.next
            pointer = pointer.next
            
        if l2:
            while l2:
                pointer.next = ListNode((l2.val+carry_over)%10)
                carry_over = (l2.val + carry_over)//10
                l2 = l2.next
                pointer = pointer.next
            
        if l1:
            while l1:
                pointer.next = ListNode((l1.val+carry_over)%10)
                carry_over = (l1.val + carry_over)//10
                l1 = l1.next
                pointer = pointer.next
            
            
        if carry_over == 1:
            pointer.next = ListNode(1)
        
        return first_node.next
