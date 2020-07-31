class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # 1.  Setup 3 pointers: left, right and curr
        left = curr = 0
        right = len(nums)-1
        
        while curr <= right:
            
            if nums[curr] == 1:
                curr += 1
                
            elif nums[curr] == 0:
                nums[curr], nums[left] = nums[left], nums[curr]
                
                curr += 1
                left += 1
            
            else:
                nums[curr], nums[right] = nums[right], nums[curr]
                right -=1
                
