class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def helper(left, right, item, output):
            
            if len(item) == 2*n:
                output.append(item)
                
            
            if left < right:
                return
            
            if left < n:
                helper(left + 1, right, item + '(', output)
                
            if right < n:
                helper(left, right+1, item + ')', output)
                
        result = []
        
        helper(0, 0, '', result)
        
        return result
