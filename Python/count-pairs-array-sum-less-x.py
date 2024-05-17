class Solution:
    def count_pairs_sorted_array_sum_less_than_x(self, nums: List[int], x: int) -> int:
        count, left, right = 0, 0,  len(nums)-1
        while left < right:
            tmp = nums[left] + nums[right]
            
            if tmp < x:
                count += right-left
                left += 1
                
            else:
                right -= 1
                
        return count
