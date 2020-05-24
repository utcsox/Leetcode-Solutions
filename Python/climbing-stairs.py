class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 0
        curr = 1
        
        result = 0
        for index in range(n):
            result = prev + curr
            prev = curr
            curr= result
            
        return result
