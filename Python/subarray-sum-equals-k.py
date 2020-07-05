# Brute Force -> not accepted
# O(n**3) time , O(n) space
# get the sums of every i, j

class Solution1:
    def subarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        cnt = 0
        
        for i in range(N):
            for j in range(i, N):
                summation = 0
                for l in range(i, j+1):
                    summation += nums[l]
                if summation == k:
                    cnt += 1
        return cnt    
    
# Using cumulative sum -> not accepted
# O(n**2) time , O(n) space
# cumulative sum of j - cumulative sum of i + value of i = cumulative sum between i and j

class Solution2:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # Intuition:  The sum between i, j is equals to:
        #             cumulative sum from 0 to j  - cumulative sum from 0 to i + nums[i]

        # Construct the cumulative sum array
        N = len(nums)
        cumu_sum = [0 for x in range(len(nums))]
        cumu_sum[0] = nums[0]

        for idx in range(1, len(nums)):
            cumu_sum[idx] = cumu_sum[idx-1] + nums[idx]

        result = 0

        for i in range(N):
            for j in range(i, N):
                sumij = cumu_sum[j] - cumu_sum[i] + nums[i]

                if sumij == k:
                    result += 1
        return result
    
    
    def subarraySum3(self, nums: List[int], k: int) -> int:
        
        count = 0
        sum_val = 0
        
        hashmap = collections.defaultdict(lambda:0)
        hashmap[0] += 1
        
        for num in nums:
            sum_val += num
            count += hashmap[sum_val-k]
    
            hashmap[sum_val] += 1
            
        return count
