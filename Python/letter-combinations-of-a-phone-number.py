# BFS
class Solution1:
    def letterCombinations(self, digits: str) -> List[str]:
        dictionary = {'2': 'abc',
              '3': 'def',
              '4': 'ghi',
              '5': 'jkl',
              '6': 'mno',
              '7': 'pqrs',
              '8': 'tuv',
              '9': 'wxyz'}
        if not digits: return []      
        ans = [""]
        for digit in digits:
            tmp = []       
            for s in ans:           
                for c in dictionary[digit]:            
                    tmp.append(s + c)     
            ans = tmp
      
        return ans
# DFS
class Solution2: 
    def letterCombinations(self, digits: str)-> List[str]:
        dictionary = {'2': 'abc',
              '3': 'def',
              '4': 'ghi',
              '5': 'jkl',
              '6': 'mno',
              '7': 'pqrs',
              '8': 'tuv',
              '9': 'wxyz'}
        
        def bfs(tmp, next_digits):
            if len(next_digits) == 0:
                output.append(tmp)
            else:
                for d in dictionary[next_digits[0]]:
                    bfs(tmp + d, next_digits[1:])
        output = []        
        if digits:
            bfs("", digits)
        return output

