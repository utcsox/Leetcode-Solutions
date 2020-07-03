class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """  
        k = - 1
        
        # 1.  Find the element stop increasing as k
        for index in range(len(nums)-1):
            if nums[index] < nums[index+1]:
                k = index
                
        # if k is sill - 1, it means we need to reverse the number
        if k == - 1:
            return nums.reverse()
        
        # 2. Identity the element from k+1 to the end that is bigger than k
        sindex = 0
        for index in range(k+1, len(nums)):
            if nums[index] > nums[k]:
                sindex = index
                 
        # 3.  Swap the element from #2 with the element from k
        # 4.  reverse the remaining elements from k+1:
        nums[k], nums[sindex] = nums[sindex], nums[k] 
        nums[k+1: ] = nums[:k:-1]
