class Solution1:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1
        
class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        level = 0
        q = deque([root])
        
        while q:
            
            for index in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
                    
            level += 1

        
        return level
