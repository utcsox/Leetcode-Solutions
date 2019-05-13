class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        index = 0
        if nums:
            for i in range(len(nums)):
                if nums[index] != nums[i]:
                    index +=1
                    nums[index] = nums[i]
            return index + 1
        else:
            return 0
