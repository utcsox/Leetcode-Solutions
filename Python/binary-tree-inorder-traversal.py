# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def helper(root, output):
            if root:
                helper(root.left, result)
                result.append(root.val)
                helper(root.right, result)
        result = []
        helper(root, result)
        return result
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        curr = root
        
        while curr is not None or stack:
            while curr is not None:
                stack.append(curr)
                curr = curr.left   

            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
            
        return result
