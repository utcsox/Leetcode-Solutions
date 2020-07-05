class Solution1:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        # Cumulative sum appraoch
        # 1.  construct an array that store cumulative sum
        # 2.  check two conditions:
        #.  a). if cumulative sum (from 0 to j - cumulative sum from 0 to i + nums[i] is equal to k 
        #   b). the value in a multiple of k, when k is not 0
        
        cumu_sum = [0 for x in range(len(nums))]
        cumu_sum[0] = nums[0]
        
        for index in range(1, len(nums)):
            cumu_sum[index] = cumu_sum[index-1] + nums[index]
        
        for i in range(len(nums)-1):
            for j in range(i + 1, len(nums)):
                tmp = cumu_sum[j] - cumu_sum[i] + nums[i]
                if tmp == k or (k != 0 and tmp % k == 0):
                    return True
                
        return False
