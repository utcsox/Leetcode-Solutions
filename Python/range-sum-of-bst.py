class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        def helper(node):
            if not node:
                return 
            
            if L <= node.val <= R:
                self.result += node.val
            
            if node.val >= L:
                helper(node.left)
                
            if node.val<= R:
                helper(node.right)
                
        self.result = 0
        helper(root)
        
        return self.result
