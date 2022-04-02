"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}
        
        def dfs(node):

            
            if node in oldToNew:
                return oldToNew[node]
            
            replica = Node(node.val)
            oldToNew[node] = replica
            
            for neighbor in node.neighbors:
                replica.neighbors.append(dfs(neighbor))
                
            return replica
        
        return dfs(node) if node else None
