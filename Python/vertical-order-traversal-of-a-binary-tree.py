# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        
        node_list = []
        
        if not root:
            return node_list
        
        def helper(node, column, row):
            
            if not node:
                return
            
            node_list.append((column, row, node.val))
            
            helper(node.left, column-1, row + 1)
            helper(node.right, column+1, row + 1)
            
        # 1.  sort the column of tuple
        helper(root, 0, 0)
        node_list.sort()
        
        output = []
        curr_column = node_list[0][0]
        curr_column_list = []
        
        # 2.  traverse each column: add node value of same column into a list
        
        
        for column, row, value in node_list:
            if column == curr_column:
                curr_column_list.append(value)
                
            else:
                output.append(curr_column_list)
                curr_column = column
                curr_column_list = [value]
                
        # 3 add the last column        
        output.append(curr_column_list)
        
        return output
