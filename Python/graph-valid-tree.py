class Solution1:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

        if n == 1:
            return True

        adj_list = collections.defaultdict(list)
        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        visited, q = set(), collections.deque([0])
        visited.add(0)

        while q:
            node = q.popleft()
            for nei in adj_list[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)

        return len(visited) == n

class Solution2:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

        if n == 1:
            return True

        adj_list = collections.defaultdict(list)
        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        visited, stack = set(), [0]
        visited.add(0)

        while stack:
            node = stack.pop()
            for nei in adj_list[node]:
                if nei not in visited:
                    visited.add(nei)
                    stack.append(nei)

        return len(visited) == n

class Solution3:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

        if n == 1:
            return True

        adj_list = collections.defaultdict(list)
        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return
            visited.add(node)
            for nei in adj_list[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        return dfs(0, -1) and n == len(visited)
