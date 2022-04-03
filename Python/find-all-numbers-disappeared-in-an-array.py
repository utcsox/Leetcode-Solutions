class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        total = len(nums)
        
        lookup = {num: 1 for num in nums}
        
        output = [index for index in range(1, total + 1) if index not in lookup]
        
        return output
