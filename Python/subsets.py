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
    
class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def dfs(first, item):

            #if the combination is done 
            if len(item) == k:
                output.append(item[:])

            for index in range(first, n):
                # Add nums[index] into the current combination
                item.append(nums[index])
                # Use the next integers to complete the combination
                dfs(index + 1, item)
                # backtrack
                item.pop()

        output = []
        n = len(nums)

        for k in range(n+1):
            dfs(0, [])

        return output
            
class Solution3:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        output = [[]]
        
        for num in nums:
            output += [curr +[num] for curr in output]
            
        return output
