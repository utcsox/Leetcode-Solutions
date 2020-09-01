# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        
        # 1.  if the root doesn't exist, return None 
        if not root: return None
        
        def helper(node, value):
            
            # 2.  if we find the node to delete, need to consider 4 different cases
            if node.val == key:
               # a).  if the node has no child, return none
                if not node: return None
                
                # b). if the node only has left child  
                if not node.right: return node.left
                
                # c).  if the node only has a right child

                if not node.left: return node.right
                
                # d).  if the node have both left/right children

                if node.left and node.right:
                    temp = root.right
                    while temp.left: temp = temp.left
                    node.val = temp.val
                    node.right = self.deleteNode(node.right, node.val)
                    
            # 3. if the current node is greater than the key, go to the left tree
            elif node.val > key:
                node.left = self.deleteNode(node.left, key)
                
            else:
                node.right = self.deleteNode(node.right, key)

            return node
        
        return helper(root, key)
