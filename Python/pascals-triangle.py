class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        if numRows == 0: 
            return result
        
        first_row = [1]
        result.append(first_row)
        
        for index in range(1, numRows):
            prev_row = result[index-1]
            current_row = [1] + (index-1)*[0] + [1]
            for j in range(1, index):
                current_row[j] = prev_row[j-1] + prev_row[j]
            
            result.append(current_row)
        return result
