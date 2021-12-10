class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        
        currMin, currMax, result = 1, 1, max(nums)
        
        for num in nums:
            
            tmpMax = max(num, num*currMin, num*currMax)
            currMin = min(num, num*currMin, num*currMax)
            currMax =  tmpMax
            
            result = max(result, currMax)
            
            
        return result
