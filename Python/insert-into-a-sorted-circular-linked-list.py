"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            new_node = Node(insertVal)
            new_node.next = new_node
            return new_node

        curr = head

        while curr.next != head:
        # Case 1.  The insert value is greater or equal to the current pointer's value
        # but less or equal to next pointer's value
            if curr.val <= insertVal <= curr.next.val:
                new_node = Node(insertVal, curr.next)
                curr.next = new_node
                return head
            
        # Case 2 The insert element is either greater than the last element or smaller than
        # first element
            elif curr.val > curr.next.val:
                if insertVal >= curr.val or insertVal <= curr.next.val:
                    new_node = Node(insertVal, curr.next)
                    curr.next = new_node

                    return head

            curr = curr.next

        # Case 3, the Link list contains uniform values
        new_node = Node(insertVal, curr.next)
        curr.next = new_node

        return head
