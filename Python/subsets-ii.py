class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result, subset = [], []
        def dfs(index):
            
            if index >= len(nums):
                result.append(subset[:])
                return

            subset.append(nums[index])
            dfs(index + 1)
            subset.pop()
            j = index + 1
            while j < len(nums) and nums[j] == nums[j-1]:
                j += 1
            dfs(j)
                        
                
        nums.sort()        
        dfs(0)
        return result
