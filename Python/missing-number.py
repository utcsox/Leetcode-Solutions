class Solution1:
    def missingNumber(self, nums: List[int]) -> int:
        
        lookup = set(nums)
        
        for index in range(len(nums)+1):
            if index not in lookup:
                return index
              
class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        
        n_list = [i for i in range(len(nums)+1)]
        
        return sum(n_list) - sum(nums)
