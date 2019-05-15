class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[len(nums)-1]:
            return len(nums)
        elif target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)):
                if nums[i] > target:
                    nums.insert(i, target)
                    return i
