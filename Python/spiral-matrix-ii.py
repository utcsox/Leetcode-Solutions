# Time:  O(n^2)
# Space: O(1)

from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # initilize the List[List[int]]
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        print(matrix)
        
        # initialie the four quadrant: left, top, right, bottom
        left, top, right, bottom, num = 0, 0, n-1, n-1, 1
        while left <= right:
            for col in range(left, right+1, 1):
                matrix[top][col] = num
                num += 1
                
            for row in range(top+1, bottom+1, 1):
                matrix[row][right] = num
                num += 1
                
            if top < bottom:
                for col in range(right-1, left-1, -1):
                    matrix[bottom][col] = num
                    num += 1
            if left < right:
                for row in range(bottom-1, top, -1):
                    matrix[row][left] = num
                    num += 1   
            left, top, right, bottom = left+1, top+1, right-1, bottom-1
        return matrix
