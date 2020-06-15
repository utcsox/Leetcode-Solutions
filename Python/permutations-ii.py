class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        def helper(nums, cur, n):
            if len(cur)== n:
                res.append(cur)
                return 

            for i in range(len(nums)):
                if not( i>0 and nums[i-1]==nums[i]):
                    #continue
                    helper(nums[:i]+nums[i+1:], cur+[nums[i]], n)
        
        n = len(nums)
        helper(nums, [], n)
        return res 
