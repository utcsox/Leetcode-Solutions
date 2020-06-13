class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def helper(first = 0):
            if first == n:
                output.append(nums[:])
            
            for index in range(first, n):
                nums[first], nums[index] = nums[index], nums[first]
                helper(first+1)
                nums[first], nums[index] = nums[index], nums[first]
                
        n = len(nums)
        output = []
        helper()
        return output
