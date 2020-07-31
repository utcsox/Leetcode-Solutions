# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        def helper(node):
            if node:
                helper(node.left)
                
                if len(result) <= k:
                    result.append(node.val)
                    
                else:
                    return
                helper(node.right)
                
        result = []
        
        helper(root)
        
        return result[k-1]
