class Solution1:
    def swapPairs(self, head: ListNode) -> ListNode:


        dummy = ListNode(-1)
        dummy.next = head
        
        prev_node = dummy

        while (head and head.next):
            first_node = head
            second_node = head.next
            
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            prev_node = first_node
            head = first_node.next
            
        return dummy.next
    
class Solution2:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if not head or not head.next:
            return head
        
        else:
            first_node = head.
            second_node = head.next
        
        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node
        
        return second_node
        
