class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:

        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # check empty matrix
        if not matrix or not matrix[0]:
            return []
        
        # Store length and width of the matrix
        N, M = len(matrix), len(matrix[0])
        
        # Initilize a defaultdict to store the items in the same diagonal
        tmp, result = defaultdict(list), []
        
        for row in range(N):
            for column in range(M):
                tmp[row+column].append(matrix[row][column])
                   
        # Add key, value pair from the tmp dictionary to result
        
        for key, values in tmp.items():
            print(key, values)
            if key % 2 == 0:
                result.extend(reversed(values))
            else:
                result.extend(values)
        
        return result
