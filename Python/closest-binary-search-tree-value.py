# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        
        def helper(node, target):
            
            if not node:
                return
            
            if abs(node.val - target) < abs(self.closest - target):
                self.closest = node.val
                
            if target < node.val:
                helper(node.left, target)
                
            else:
                helper(node.right, target)
            

        self.closest = root.val
        helper(root, target)
        
        return self.closest
