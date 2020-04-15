# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        tmp = head
        list_count = 0
        while tmp is not None:
            tmp = tmp.next
            list_count += 1
        
        k = list_count - n
        
        curr = head
        prev = None
        
        while k > 0:
            prev = curr
            curr = curr.next
            k = k-1
        
        # if the node to remove is the first one
        if prev is None:
            return head.next
        else:
            prev.next = curr.next
            curr.next = None
            
            return head
            
        
