class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        tmp = [None] * len(nums)
        for i in range(len(nums)):
            tmp[(i+k)%len(nums)] = nums[i]
        
        nums[:] = tmp
