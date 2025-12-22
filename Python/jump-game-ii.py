class Solution:
    def jump(self, nums: List[int]) -> int:

        curr_end, curr_far, res = 0, 0, 0

        for i in range(len(nums) - 1):

            curr_far = max(curr_far, i + nums[i])

            if i == curr_end:
                res += 1
                curr_end = curr_far

        return res
  
