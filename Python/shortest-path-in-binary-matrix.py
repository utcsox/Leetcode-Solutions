class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        queue = deque([(0, 0, 1)])
        visit = set()
        directions = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1),\
                      (-1, 1)]

        while queue:
            r, c, l = queue.popleft()
            if (min(r, c) < 0 or max(r, c) >= N or grid[r][c] == 1):
                continue

            if r == N - 1 and c == N - 1:
                return l

            for dr, dc in directions:
                if (r + dr, c + dc) not in visit:
                    queue.append((r + dr, c + dc, l + 1))
                    visit.add((r + dr, c + dc))

        return -1
