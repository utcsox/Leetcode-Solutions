class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        tmp = [None] * len(nums)
        for i in range(len(nums)):
            tmp[(i+k)%len(nums)] = nums[i]
        
        nums[:] = tmp
        
        
class Solution2:
    def reverse(self, nums, beg, end):
        while(beg < end):
            nums[beg], nums[end] = nums[end], nums[beg]
            beg, end = beg + 1, end - 1
            
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k%=n
        
        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)
