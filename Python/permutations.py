class Solution1:
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
    
class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if (nums == None or len(nums)<=1):
            return [nums]

        result = []
        n = len(nums)

        def helper(nums, tmp, n):
            if len(tmp) == n:
                result.append(tmp[:])
                return

            for index in range(len(nums)):
                if nums[index] not in tmp:
                    helper(nums, tmp + [nums[index]], n)

        helper(nums, [], n)
        return result    
