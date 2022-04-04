class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        output = []
        
        for index in range(len(nums)):
            
            tmp = abs(nums[index])
            if nums[tmp-1] < 0:
                output.append(tmp)
            
            else:
                nums[tmp-1] *= -1
            
        return output
