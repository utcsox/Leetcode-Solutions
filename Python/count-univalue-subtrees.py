# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def helper(node):
            
            if not node:
                return 0, True

            left_count, is_left_uni = helper(node.left)
            right_count, is_right_uni = helper(node.right)  
            
            if (not node.left and not node.right):
                return (left_count + right_count + 1, True)
            
            is_uni = True
            
            if node.left:
                is_uni = is_left_uni and is_uni and node.left.val == node.val
            
            if node.right:
                is_uni = is_right_uni and is_uni and node.right.val == node.val

            if is_uni:
                return (left_count + right_count + 1, True)
            
            else:
                return (left_count + right_count, False)
        
        total_count, is_unival = helper(root)
        return total_count


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def countUnivalSubtrees(self, root: TreeNode) -> int:

        def helper(node):
            
            if not node:
                return 0, True
            
            if (not node.left and not node.right):
                is_uni, self.count = 1, self.count + 1
                
            left_count, is_left_uni = helper(node.left)
            right_count, is_right_uni = helper(node.right)   
            is_uni = True
            
            if not is_left_uni or not is_right_uni:
                is_uni = False
            
            if node.left and node.left.val != node.val:
                is_uni = False
            
            if node.right and node.right.val != node.val:
                
                is_uni = False
            
            if is_uni:
                return (left_count + right_count + 1, True)
            
            else:
                return (left_count + right_count, False)
        
        self.count = 0
        total_count, is_unival = helper(root)
        return total_count
