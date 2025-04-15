# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        if not root:
            return -1

        res = float("inf")

        def helper(node):
        
            nonlocal res
            if not node:
                return 

            diff = abs(node.val - target)

            if abs(res - target) == diff:
                res = min(res, node.val)

            if abs(res - target) > diff:
                res = node.val

            if node.val < target:
                helper(node.right)

            if node.val > target:
                helper(node.left)

            return res

        return helper(root)
        
