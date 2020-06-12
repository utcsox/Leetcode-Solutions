# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower = float('-inf'), upper = float('inf')):
            if node is None:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            
            if helper(node.right, node.val, upper) == False:
                return False
            
            if helper(node.left, lower, node.val) == False:
                return False
            
            return True
        
        return helper(root)

class Solution2:
    def isValidBST(self, root: TreeNode) -> bool:
        
        stack, inorder = [], float('-inf')
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
            
        return True
