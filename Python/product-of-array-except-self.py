class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        result = []
        left = [1] + [0] * (len(nums)-1)
        right = [0] * (len(nums)-1) + [1]
        
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
        for j in range(len(nums)-2, -1, -1):
            right[j] = right[j+1] * nums[j+1]
        
        for index in range(len(nums)):
            result.append(left[index]*right[index])
            
    
        return result
