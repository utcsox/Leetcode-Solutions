class Solution1:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cumu_sum = [0] * len(nums)
        cumu_sum[0] = nums[0]
        
        for index in range(1, len(nums)):
            cumu_sum[index] = cumu_sum[index-1] + nums[index]
            
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                tmp = cumu_sum[j] - cumu_sum[i] + nums[i]
                if ((tmp == k) or (k!=0 and tmp%k==0)):
                    return True
                
        return False
