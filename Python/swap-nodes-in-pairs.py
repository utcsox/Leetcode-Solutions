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
        
