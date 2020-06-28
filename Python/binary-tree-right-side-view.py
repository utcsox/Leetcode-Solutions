# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        
        result = []
        
        if not root:
            return result
        
        
        def helper(node, level):
            
            if not node:
                return
            
            if len(result) == level:
                #result.append(node.val)
                result.append([])
            result[level].append(node.val)
                
            helper(node.right, level+1)
            helper(node.left, level+1)
            
        helper(root, 0)
        
        #return result
        return [x[0] for x in result]
