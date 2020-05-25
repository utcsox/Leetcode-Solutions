# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if root == None:
            return result
        if root:
            result.append(root.val)
            result = result + self.preorderTraversal(root.left)
            result = result + self.preorderTraversal(root.right)
        return result
    
class Solution2:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        result = []
        stack = [root]
        
        while stack:
            root = stack.pop()
            if root:
                result.append(root.val)
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
        return result
