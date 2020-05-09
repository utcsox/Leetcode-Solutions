class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        storage = {}
        for num in nums:
            if num in storage:
                return True
            else:
                storage[num] = 1
        return False
 
# Time:  O(n)
# Space: O(n)

class Solution2(object):
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        return len(nums) > len(set(nums))
