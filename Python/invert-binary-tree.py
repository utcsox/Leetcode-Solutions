class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def helper(root):
            
            if not root:
                return None
            
            tmp = root.left
            root.left = root.right
            root.right = tmp
            
            helper(root.left)
            helper(root.right)
            
            
        helper(root)
        
        return root
