class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
        local_max, global_max = 0, 0
        for num in nums:
            local_max = max(0, local_max + num)
            global_max = max(local_max, global_max)
        return global_max
    
class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        #initialize an array
        dp = [0] * len(nums)
        dp[0] = nums[0]
        
        for index in range(1, len(nums)):
            dp[index] = max(dp[index-1] + nums[index], nums[index])
            
        return max(dp)
