class Solution:
    def minMoves(self, nums: List[int]) -> int:
        
        min_element, output = min(nums), 0
        
        for num in nums:
            output += num - min_element
            
        return output
