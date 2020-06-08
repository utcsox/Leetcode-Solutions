class Solution1:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        for row in matrix:
            if target in row:
                return True
        return False

class Solution2:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # setup bottom left
        row_num = len(matrix)
        col_num = len(matrix[0])

        row, col = len(matrix)-1, 0
        while row >= 0 and col < col_num:
            if matrix[row][col] < target:
                col = col + 1
            elif matrix[row][col] > target:
                row = row-1
            else:
                return True
        return False
