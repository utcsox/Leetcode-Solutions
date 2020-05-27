class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = 0
        sum_val = 0
        
        hashmap = collections.defaultdict(lambda:0)
        hashmap[0] += 1
        
        for num in nums:
            sum_val += num
            count += hashmap[sum_val-k]
    
            hashmap[sum_val] += 1
            
        return count
