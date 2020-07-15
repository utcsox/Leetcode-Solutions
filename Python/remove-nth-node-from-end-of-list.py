# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1:
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
            
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution2:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        
        slow = fast = dummy
        
        # fast is n spot faster
        for _ in range(n):
            fast = fast.next
            
        while fast.next:
            slow = slow.next
            fast = fast.next
            
        slow.next = slow.next.next
        
        return dummy.next
