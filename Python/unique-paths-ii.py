class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        matrix = [[0 for j in range(n)]for i in range(m)]
        
        # 0 column
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            else:
                matrix[i][0] = 1
        # 0 row
        
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            else:
                matrix[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                else:
                    matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        return matrix[m-1][n-1]
        
        
