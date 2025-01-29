# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        mapping = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            node, position = queue.popleft()
            mapping[position].append(node.val)

            if node.left:
                queue.append((node.left, position - 1))

            if node.right:
                queue.append((node.right, position + 1))

        sorted_keys = sorted(list(mapping.keys()))
        result = [mapping[x] for x in sorted_keys]

        return result
        
