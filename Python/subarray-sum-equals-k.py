# Brute Force -> not accepted
# O(3) time , O(n) space
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
