# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        output = []
        
        if not root:
            return output
        
        def helper(node, level):
            # start at the current level
            if len(output) == level:
                output.append([])
            #append the current node values
            output[level].append(node.val)
            
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
                         
        helper(root, 0)
        
        return output
