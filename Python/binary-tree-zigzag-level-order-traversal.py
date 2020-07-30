# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        output = []
        if not root:
            return
        
        
        def helper(node, level):
            
            if not node:
                return
            
            if len(output) == level:
                output.append(deque([node.val]))
            
            else:
                if level % 2 == 0:
                    output[level].append(node.val)
                    
                else:
                    output[level].appendleft(node.val)
            
            if node.left:
                helper(node.left, level+1)
                
            if node.right:
                helper(node.right, level+1)
                
        output = []
        helper(root, 0)
        
        return output
