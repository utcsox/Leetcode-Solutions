class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        graph = collections.defaultdict(list)

        for account in accounts:
            name = account[0]
            for email in account[2:]:
                graph[email].append(account[1])
                graph[account[1]].append(email)

        visited = set()
        res = []

        for account in accounts:
            name = account[0]
            emails = account[1:]

            if emails[0] in visited:
                continue
            else:
                stack = [emails[0]]
                visited.add(emails[0])

                local_res = []
                while stack:
                    node = stack.pop()
                    local_res.append(node)
                    for edge in graph[node]:
                        if edge not in visited:
                            stack.append(edge)
                            visited.add(edge)

                res.append([name] + sorted(local_res))

        return res
  
