# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        if root is None:
            return []
        
        if root:
            res = res + self.inorderTraversal(root.left)
            res.append(root.val)
            res = res + self.inorderTraversal(root.right)

        return res
