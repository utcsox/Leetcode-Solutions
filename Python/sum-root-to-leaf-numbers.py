# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def helper(node, output):
            if not node:
                return 0

            output = 10 * output + node.val

            if not node.left and not node.right:
                return output

            return helper(node.left, output) + helper(node.right, output)

        return helper(root, 0)
        
