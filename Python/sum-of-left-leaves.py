class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        result = 0
        if root is not None:
            if root.left != None and (root.left.left == None and root.left.right == None):
                result += root.left.val + self.sumOfLeftLeaves(root.right)
            else:
                result = self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

        return result
