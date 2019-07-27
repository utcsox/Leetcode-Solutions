class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        nums = sorted(nums)
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums)-1
            if i > 0 and nums[i-1]== nums[i]:
                continue
            while j < k:
                _sum = nums[i] + nums[j] + nums[k]
                if _sum < 0:
                    j += 1
                elif _sum > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    
                    while j<k and nums[j] == nums[j+1]:
                        j = j +1
                    while j< k and nums[k] == nums[k-1]:
                        k = k -1
                    j += 1
                    k -= 1
                    
        return result
