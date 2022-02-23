class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        rob1, rob2 = 0 , 0
        
        for index in range(len(nums)):
            tmp = max(rob2, rob1 + nums[index])
            rob1 = rob2
            rob2 = tmp
            
        return rob2
