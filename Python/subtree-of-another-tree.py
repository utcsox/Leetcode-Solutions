# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helper(s, t):

            if not s and not t:
                return True

            if s and t and s.val == t.val:
                return (helper(s.left, t.left) and
                        helper(s.right, t.right))

            return False
        
        if not subRoot: 
            return True
        if not root and subRoot:
            return False
        
        if helper(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or
        self.isSubtree(root.right, subRoot))
        
