class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        if len(nums) == 0:
            return 0

        if len(nums) <= k:
            return sum(nums)/len(nums)

        res, total =  sum(nums[:k]), sum(nums[:k])

        for i in range(k, len(nums)):
            total += nums[i]
            total -= nums[i - k]
            res = max(res, total)

        return res/k
