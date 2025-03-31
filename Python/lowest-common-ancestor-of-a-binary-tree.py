# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(node,  p, q):

            if not node:
                return None
            
            if node == p or node == q:
                return node
            
            left = helper(node.left, p, q)
            right = helper(node.right, p, q)
            
            if left and right:
                return node
            
            if not left:
                return right
            
            if not right:
                return left
            
        return helper(root, p, q)
        
class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        parents = {root: None}

        stack = [root]

        while stack:
            node = stack.pop()
            if node.left:
                parents[node.left] = node
                stack.append(node.left)


            if node.right:
                parents[node.right] = node
                stack.append(node.right)

        ancestors = set()

        p_cp, q_cp = p, q

        while p_cp != q_cp:
            if p_cp:
                p_cp = parents[p_cp]

            else:
                p_cp = q

            if q_cp:
                q_cp = parents[q_cp]

            else:
                q_cp = p

        return p_cp


        # while p:
        #     ancestors.add(p)
        #     p = parents[p]

        # while q:
        #     if q in ancestors:
        #         return q

        #     q = parents[q]
            
