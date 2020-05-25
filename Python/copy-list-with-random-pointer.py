"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution1:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        dummy = Node(0)
        prev = dummy
        curr = head
        hashmap = {}
        
        while(curr):
            replica = Node(curr.val)
            hashmap[curr] = replica
            prev.next = replica
            prev = prev.next
            curr = curr.next
            
        curr = head
        
        while(curr):
            if curr.random:
                hashmap[curr].random = hashmap[curr.random]
            curr = curr.next
            
        return dummy.next
