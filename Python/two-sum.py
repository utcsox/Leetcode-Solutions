class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for idx, num in enumerate(nums):
            if (target - num) in nums[idx+1:]:
    
                return [idx, nums[idx+1:].index(target-num) + idx + 1] 
    
    def twoSum2(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in nums:
        j = target - i
        start_index = nums.index(i)
        future_index = nums.index(i)+ 1
        for j in nums[future_index:]:
            if j == target - i:
                return [start_index, nums[future_index:].index(j) + start_index + 1]
