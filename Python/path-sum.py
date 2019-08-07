class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        
        if root.left is None and root.right is None and root.val-sum==0:
            return True
        
        else:
            sum = sum - root.val
            left = self.hasPathSum(root.left, sum)
            right = self.hasPathSum(root.right, sum)
        
        return left or right
