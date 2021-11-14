class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows, columns = len(board), len(board[0])  
        path = set()
        
        def dfs(r, c, index):
            
            if index == len(word):
                return True
            
            if (r < 0 or c <0 or \
               r >= rows or c >= columns or word[index] != board[r][c] or (r,c) in path): 
                return False
            
            path.add((r, c))
            
            # run dfs in all four adjecent positions
            result = (dfs(r + 1, c, index + 1) or 
                      dfs(r - 1, c, index + 1) or
                      dfs(r, c - 1, index + 1) or
                      dfs(r, c + 1, index + 1))
                     
            path.remove((r, c))
            return result
        
        for row in range(rows):
            for column in range(columns):
                if dfs(row, column, 0):
                    return True
                
                

        return False
