class Solution1:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums)):
            if nums[i-1] == nums[i]:
                return nums[i]

class Solution2:
    def findDuplicate(self, nums: List[int]) -> int:
        
        seen = set()
        
        for num in nums:
            
            if num in seen:
                return num
            
            seen.add(num)
