class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix:
            return False
        
        total_rows, total_columns = len(matrix), len(matrix[0])
        left, right = 0, total_rows*total_columns-1
        
        while left <= right:
            
            pivot_index = (left+right)//2
            pivot_value = matrix[pivot_index//total_columns][pivot_index%total_columns]
            
            if pivot_value == target:
                return True
            
            elif target < pivot_value:
                right = pivot_index - 1
                
                
            else:
                left = pivot_index + 1
                
        return False
