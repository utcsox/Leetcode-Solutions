# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        if head == None or head.next == None:
            return head
        
        l1, slow, fast, prev = head, head, head, None
        
        while fast is not None and fast.next is not None: 
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # prev is end of l1, slow is head of l2
        # need to reverse l2
        
        prev.next = None
        
        l2prev = None
        l2head = slow
        
        while l2head != None:
            nxt = l2head.next
            l2head.next = l2prev
            l2prev = l2head
            l2head = nxt
            
        dummy = ListNode(0)
        current = dummy
        
        while l1 is not None and l2prev is not None:
            current.next = l1
            current = l1
            l1 = l1.next
            
            current.next = l2prev
            current = l2prev
            l2prev = l2prev.next
            
        return dummy.next
            
        
        
        
