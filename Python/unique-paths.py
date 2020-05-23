class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[1 for j in range(m)] for i in range(n)]
        
        for i in range(1, n):
            for j in range(1, m):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        return matrix[n-1][m-1]
