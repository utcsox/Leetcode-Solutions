class Solution1:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        from collections import deque
        
        num_rows, num_columns = len(heights), len(heights[0])

        pacific_q, atlantic_q = deque(), deque()

        for i in range(num_rows):
            pacific_q.append((i, 0))
            atlantic_q.append((i, num_columns - 1))

        for i in range(num_columns):
            pacific_q.append((0, i))
            atlantic_q.append((num_rows - 1, i))


        def bfs(q):
            seen = set()
            while q:
                r, c = q.popleft()
                seen.add((r, c))
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    if new_r < 0 or new_c < 0 or new_r >= num_rows or new_c >= num_columns \
                        or (new_r, new_c) in seen or heights[new_r][new_c] < heights[r][c]:
                        continue

                    q.append((new_r, new_c))
                    
            return seen

        pacific = bfs(pacific_q)
        atlantic = bfs(atlantic_q)


        return list(pacific.intersection(atlantic))

class Solution2:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        from collections import deque
        
        num_rows, num_columns = len(heights), len(heights[0])

        pacific, atlantic = set(), set()

        def dfs(row, col, seen):
            seen.add((row, col))
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                new_r, new_c = row + dr, col + dc
                if new_r < 0 or new_c < 0 or new_r >= num_rows or new_c >= num_columns \
                        or (new_r, new_c) in seen or heights[new_r][new_c] < heights[row][col]:
                        continue

                dfs(new_r, new_c, seen)

        for i in range(num_rows):
            dfs(i, 0, pacific)
            dfs(i, num_columns - 1, atlantic)

        for i in range(num_columns):
            dfs(0, i, pacific)
            dfs(num_rows - 1, i, atlantic)

        return list(pacific.intersection(atlantic))
