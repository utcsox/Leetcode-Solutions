class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # This problem can be solved by multiple product of left and right of itself
        # 1.  Create left/right array that 
    
        output = []
        if len(nums) == 0:
            return output
        
        # initialize the empty array for the left/right side
        left = [0 for x in range(len(nums))]
        right = [0 for x in range(len(nums))]
        
        left[0] = 1
        right[-1] = 1
        
        # The current value =  previous value of input array * the product of the array before current value
        for index in range(1, len(nums)):
            left[index] = left[index-1] * nums[index-1]
            
        for index in range(len(nums)-2, -1, -1):
            right[index] = right[index+1]* nums[index+1]
            
        for index in range(len(nums)):
            output.append(left[index] * right[index])
            
        return output
