# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
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
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution2:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        output = []
        
        if not root:
            return output
        
        level = 0
        queue = deque([root, ])
        
        while queue:
            output.append([])
            num_elements_level = len(queue)
            
            for index in range(num_elements_level):
                node = queue.popleft()
                output[level].append(node.val)
                
                # add left child into the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return output
