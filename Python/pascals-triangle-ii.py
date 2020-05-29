class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]
        if rowIndex == 0:
            return result
        
        for index in range(1, rowIndex+1):
            prev_row = result[index-1]
            cur_row = [1] + (index-1)*[0] + [1]
            for num in range(1, index):
                cur_row[num] = prev_row[num-1] + prev_row[num]
            result.append(cur_row)
            
        return cur_row
