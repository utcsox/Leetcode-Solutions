# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root or not target:
            return []

        graph = collections.defaultdict(list)
        deque = collections.deque([root])
        while deque:
            node = deque.popleft()
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                deque.append(node.left)

            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                deque.append(node.right)

        visited = set([target])
        deque = collections.deque([(target, 0)])
        result = []

        while deque:
            node, distance = deque.popleft()
            if distance == k:
                result.append(node.val)

            else:
                for edge in graph[node]:
                    if edge not in visited:
                        visited.add(edge)
                        deque.append((edge, distance + 1))


        return result

        
        return result



        return []
