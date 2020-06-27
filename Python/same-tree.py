# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        def helper(p, q):
            
            # both p and q are None
            if not p and not q:
                return True

            # q or p is None
            if not q or not p:
                return False

            # if p and q have different value 
            if p.val != q.val:
                return False

            # check recursion
            return helper(p.left, q.left) and helper(p.right, q.right)

        return helper(p, q)
