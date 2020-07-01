class Solution1:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        def helper(nums, item, index):
            result.append(item[:])

            for index in range(index, len(nums)):
                item.append(nums[index])
                helper(nums, item, index+1)
                item.pop()

        helper(nums, [], 0)
        
        return result
            
