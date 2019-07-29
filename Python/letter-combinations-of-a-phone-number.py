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
        d = [" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv","wxyz"]
        ans = [""]
        for digit in digits:
            tmp = []       
            for s in ans:           
                for c in dictionary[digit]:            
                    tmp.append(s + c)     
            ans = tmp
      
        return ans
