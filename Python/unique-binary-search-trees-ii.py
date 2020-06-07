# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def helper(start, end):
            result= []
            if start > end:
                result.append(None,)

            # pick a root out of possible n
            for index in range(start, end + 1):
                left_trees = helper(start, index-1)
                right_trees = helper(index+1, end)

                for r in right_trees:                   
                    for l in left_trees:
                        current_tree = TreeNode(index)
                        current_tree.left = l
                        current_tree.right = r
                        result.append(current_tree)

            return result
        if n == 0:
            return []
        return helper(1, n)
