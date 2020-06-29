# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(node,  p, q):

            if not node:
                return None
            
            if node == p or node == q:
                return node
            
            left = helper(node.left, p, q)
            right = helper(node.right, p, q)
            
            if left and right:
                return node
            
            if not left:
                return right
            
            if not right:
                return left
            
        return helper(root, p, q)
