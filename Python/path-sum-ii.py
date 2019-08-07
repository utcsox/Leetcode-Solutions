# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        
        result = []
        def helper(root, curr_list, curr_sum):
            if root == None:
                return 
            if root.left == None and root.right == None:
                if curr_sum + root.val == sum:
                    result.append(curr_list + [root.val])
            else:
                helper(root.left, curr_list + [root.val] , curr_sum + root.val)
                helper(root.right, curr_list+ [root.val] , curr_sum + root.val)
        
        helper(root, [], 0)
        
        return result
