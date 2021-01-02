class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
  
        if not nums or sum(nums)<s:
            return 0
        
        current_sum, left, min_length = 0, 0, len(nums)
        
        for right in range(len(nums)):
            current_sum += nums[right]
            
            while current_sum >= s:
                min_length = min(min_length, right-left + 1)
                current_sum -= nums[left]
                left += 1
                
        return min_length
