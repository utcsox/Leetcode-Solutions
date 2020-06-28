# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        if not root:
            return False
        
        def helper(root, total):
            if not root:
                return False
            
            total += root.val
            if not root.left and not root.right:
                return total == sum
            
            return helper(root.left, total) or helper (root.right, total)
        
        return helper(root, 0)
