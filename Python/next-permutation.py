class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """  

        pivot, swap = -1, -1

        # 1.  Find the element stop increasing as the pivot
        for index in range(len(nums) - 1):
            if nums[index + 1] > nums[index]:
                pivot = index

        # 2.  If the list is strictly decreasing, return the reverse
        if pivot == -1:
            return nums.reverse()

        # 3.  Identify the swap index to swap with the pivot index
        for index in range(pivot + 1, len(nums)):
            if nums[index] > nums[pivot]:
                swap = index

        # 4.  Swap the index between pivot and swap
        # 5.  reverse the remaining elements from k+1: to end
        
        nums[pivot], nums[swap] = nums[swap], nums[pivot]
        nums[pivot + 1:] = reversed(nums[pivot + 1:])
