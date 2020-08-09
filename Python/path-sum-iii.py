# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.count = 0
        if not root:
            return self.count
        
        def helper(node, curr_sum):
            
            if not node:
                return
            
            curr_sum += node.val
            
            # situation 1
            
            if curr_sum == sum:
                self.count += 1
            
            # situation 2
            self.count += lookup[curr_sum- sum]
            
            lookup[curr_sum] += 1
            
            helper(node.left, curr_sum)
            helper(node.right, curr_sum)
            
            lookup[curr_sum] -= 1
            

        lookup = defaultdict(int)
        helper(root, 0)
        
        return self.count
