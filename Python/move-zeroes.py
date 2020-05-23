class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums))[::-1]:
            if nums[i] == 0:
                nums.extend([nums[i]])
                del nums[i]
        
class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[pointer] =  nums[i]
                pointer += 1
        for i in range(pointer, len(nums)):
            nums[i] = 0
            
class Solution3:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for i in range(len(nums))[::-1]:
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
        return nums
