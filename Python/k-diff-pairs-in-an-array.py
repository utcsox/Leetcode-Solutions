class Solution1:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = 0
        lookup = Counter(nums)
        
        for key, value in lookup.items():
            if k >0 and key + k in lookup:
                count += 1
                
            elif k==0 and lookup[key] > 1:
                count += 1
                
        return count
      
class Solution2:
   def findPairs(self, nums: List[int], k: int) -> int:
       nums.sort()
        
       left, right, count = 0 , 1, 0
        
       while left < len(nums) and right < len(nums):
           if left == right or (nums[right]- nums[left]) < k:
               right += 1
                
           elif nums[right] - nums[left]  > k:
               left += 1
                
           else:
               count+= 1
               left += 1
                
           while (left < len(nums) and nums[left-1] == nums[left]):
               left += 1
                
       return count
