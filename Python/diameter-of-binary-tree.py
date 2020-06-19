
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def helper(node, path):
            if not node:
                return
            path += str(node.val)
            if not node.left and not node.right:
                result.append(path)
            if node.left:
                helper(node.left, path + '->')
                
            if node.right:
                helper(node.right, path + '->')
                    
        result = []

        
        helper(root, '')
        
        return result
