class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        output = 0
        #1.  sort the nums array
        nums.sort()
        
        #2.  find the median
        
        median = nums[len(nums)//2]
        
        # sum of absolute difference between median and n
        
        for num in nums:
            output += abs(num-median)
            
        return output
