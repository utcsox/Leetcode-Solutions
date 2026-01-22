class Solution1:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj_list, visited, components = defaultdict(list), set(), 0
        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        def dfs(node):
            if node not in visited:
                visited.add(node)
            for nei in adj_list[node]:
                if nei not in visited:
                    dfs(nei)

        for i in range(n):
            if i not in visited:
                components += 1
                dfs(i)

        return components

class Solution2:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        components, visited = 0, set()

        for i in range(n):
            if i not in visited:
                components += 1
                stack = [i]
                while stack:
                    node = stack.pop()
                    for nei in adj_list[node]:
                        if nei not in visited:
                            visited.add(nei)
                            stack.append(nei)

        return components

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        components, visited = 0, set()

        for i in range(n):
            if i not in visited:
                components += 1
                q = collections.deque([i])
                while q:
                    node = q.popleft()
                    for nei in adj_list[node]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)

        return components

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        components, visited = 0, set()

        for i in range(n):
            if i not in visited:
                components += 1
                q = collections.deque([i])
                while q:
                    node = q.popleft()
                    for nei in adj_list[node]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)

        return components


class Solution3:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        components, visited = 0, set()

        for i in range(n):
            if i not in visited:
                components += 1
                q = collections.deque([i])
                while q:
                    node = q.popleft()
                    for nei in adj_list[node]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)

        return components

 
